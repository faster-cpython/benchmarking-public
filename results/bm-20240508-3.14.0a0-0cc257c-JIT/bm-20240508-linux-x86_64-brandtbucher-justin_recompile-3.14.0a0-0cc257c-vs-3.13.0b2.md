# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_recompile
- machine: linux-x86_64
- commit hash: 0cc257c
- commit date: 2024-05-08
- overall geometric mean: 1.08x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 302 ms: 1.10x slower                                                    |
| chameleon      | 7.22 ms                                                    | 7.11 ms: 1.02x faster                                                   |
| docutils       | 2.83 sec                                                   | 3.83 sec: 1.36x slower                                                  |
| html5lib       | 67.2 ms                                                    | 75.0 ms: 1.12x slower                                                   |
| tornado_http   | 94.6 ms                                                    | 99.4 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                      | 1.11x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 718 ms: 1.22x slower                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 754 ms: 1.23x slower                                                    |
| async_tree_io              | 939 ms                                                     | 1.18 sec: 1.25x slower                                                  |
| async_tree_none            | 378 ms                                                     | 489 ms: 1.29x slower                                                    |
| async_tree_io_tg           | 936 ms                                                     | 1.21 sec: 1.29x slower                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 588 ms: 1.33x slower                                                    |
| async_tree_memoization     | 463 ms                                                     | 618 ms: 1.33x slower                                                    |
| async_tree_none_tg         | 336 ms                                                     | 467 ms: 1.39x slower                                                    |
| Geometric mean             | (ref)                                                      | 1.29x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 81.0 ms: 1.09x faster                                                   |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                    |
| float          | 78.9 ms                                                    | 89.8 ms: 1.14x slower                                                   |
| Geometric mean | (ref)                                                      | 1.01x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 224 ms: 1.01x slower                                                    |
| regex_compile  | 137 ms                                                     | 140 ms: 1.02x slower                                                    |
| regex_v8       | 25.1 ms                                                    | 25.8 ms: 1.03x slower                                                   |
| regex_effbot   | 3.67 ms                                                    | 3.85 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                      | 1.03x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 2.02 sec: 1.05x faster                                                  |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                   |
| pickle_dict          | 34.8 us                                                    | 34.2 us: 1.02x faster                                                   |
| unpickle_list        | 5.34 us                                                    | 5.26 us: 1.02x faster                                                   |
| json_loads           | 28.9 us                                                    | 28.7 us: 1.01x faster                                                   |
| unpickle             | 15.1 us                                                    | 15.2 us: 1.00x slower                                                   |
| pickle_pure_python   | 305 us                                                     | 307 us: 1.01x slower                                                    |
| unpickle_pure_python | 218 us                                                     | 224 us: 1.03x slower                                                    |
| pickle               | 11.5 us                                                    | 12.0 us: 1.05x slower                                                   |
| xml_etree_generate   | 87.4 ms                                                    | 93.2 ms: 1.07x slower                                                   |
| pickle_list          | 5.11 us                                                    | 5.46 us: 1.07x slower                                                   |
| xml_etree_parse      | 162 ms                                                     | 174 ms: 1.08x slower                                                    |
| xml_etree_process    | 61.2 ms                                                    | 66.2 ms: 1.08x slower                                                   |
| xml_etree_iterparse  | 107 ms                                                     | 140 ms: 1.30x slower                                                    |
| Geometric mean       | (ref)                                                      | 1.04x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.1 ms: 1.03x slower                                                   |
| python_startup_no_site | 7.11 ms                                                    | 7.68 ms: 1.08x slower                                                   |
| Geometric mean         | (ref)                                                      | 1.06x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.72 ms: 1.16x faster                                                   |
| django_template | 34.8 ms                                                    | 36.4 ms: 1.05x slower                                                   |
| genshi_text     | 23.7 ms                                                    | 25.2 ms: 1.07x slower                                                   |
| genshi_xml      | 51.6 ms                                                    | 61.3 ms: 1.19x slower                                                   |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| scimark_fft                | 392 ms                                                     | 318 ms: 1.23x faster                                                    |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.54 ms: 1.16x faster                                                   |
| richards                   | 50.9 ms                                                    | 44.0 ms: 1.16x faster                                                   |
| mako                       | 11.2 ms                                                    | 9.72 ms: 1.16x faster                                                   |
| crypto_pyaes               | 77.5 ms                                                    | 67.6 ms: 1.15x faster                                                   |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.14x faster                                                    |
| richards_super             | 57.4 ms                                                    | 50.5 ms: 1.14x faster                                                   |
| fannkuch                   | 402 ms                                                     | 363 ms: 1.11x faster                                                    |
| pyflate                    | 484 ms                                                     | 444 ms: 1.09x faster                                                    |
| nbody                      | 88.3 ms                                                    | 81.0 ms: 1.09x faster                                                   |
| scimark_monte_carlo        | 69.2 ms                                                    | 64.1 ms: 1.08x faster                                                   |
| pprint_safe_repr           | 758 ms                                                     | 714 ms: 1.06x faster                                                    |
| deepcopy_memo              | 39.7 us                                                    | 37.7 us: 1.05x faster                                                   |
| tomli_loads                | 2.12 sec                                                   | 2.02 sec: 1.05x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                                  |
| sqlite_synth               | 2.99 us                                                    | 2.85 us: 1.05x faster                                                   |
| chaos                      | 61.3 ms                                                    | 58.8 ms: 1.04x faster                                                   |
| coverage                   | 93.1 ms                                                    | 89.6 ms: 1.04x faster                                                   |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                   |
| pickle_dict                | 34.8 us                                                    | 34.2 us: 1.02x faster                                                   |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                                    |
| unpickle_list              | 5.34 us                                                    | 5.26 us: 1.02x faster                                                   |
| chameleon                  | 7.22 ms                                                    | 7.11 ms: 1.02x faster                                                   |
| thrift                     | 823 us                                                     | 814 us: 1.01x faster                                                    |
| json_loads                 | 28.9 us                                                    | 28.7 us: 1.01x faster                                                   |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                                   |
| asyncio_websockets         | 567 ms                                                     | 564 ms: 1.00x faster                                                    |
| meteor_contest             | 110 ms                                                     | 109 ms: 1.00x faster                                                    |
| mdp                        | 2.79 sec                                                   | 2.80 sec: 1.00x slower                                                  |
| unpickle                   | 15.1 us                                                    | 15.2 us: 1.00x slower                                                   |
| pickle_pure_python         | 305 us                                                     | 307 us: 1.01x slower                                                    |
| generators                 | 29.6 ms                                                    | 29.9 ms: 1.01x slower                                                   |
| bench_mp_pool              | 23.9 ms                                                    | 24.1 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 3.39 us: 1.01x slower                                                   |
| scimark_sor                | 127 ms                                                     | 129 ms: 1.01x slower                                                    |
| comprehensions             | 16.6 us                                                    | 16.8 us: 1.01x slower                                                   |
| asyncio_tcp                | 508 ms                                                     | 515 ms: 1.01x slower                                                    |
| regex_dna                  | 221 ms                                                     | 224 ms: 1.01x slower                                                    |
| deepcopy                   | 367 us                                                     | 374 us: 1.02x slower                                                    |
| regex_compile              | 137 ms                                                     | 140 ms: 1.02x slower                                                    |
| logging_silent             | 105 ns                                                     | 107 ns: 1.03x slower                                                    |
| scimark_lu                 | 122 ms                                                     | 125 ms: 1.03x slower                                                    |
| unpickle_pure_python       | 218 us                                                     | 224 us: 1.03x slower                                                    |
| regex_v8                   | 25.1 ms                                                    | 25.8 ms: 1.03x slower                                                   |
| python_startup             | 10.8 ms                                                    | 11.1 ms: 1.03x slower                                                   |
| dulwich_log                | 67.2 ms                                                    | 69.4 ms: 1.03x slower                                                   |
| pathlib                    | 17.3 ms                                                    | 17.9 ms: 1.04x slower                                                   |
| sqlglot_normalize          | 110 ms                                                     | 115 ms: 1.04x slower                                                    |
| go                         | 145 ms                                                     | 151 ms: 1.04x slower                                                    |
| bench_thread_pool          | 834 us                                                     | 871 us: 1.04x slower                                                    |
| hexiom                     | 6.30 ms                                                    | 6.58 ms: 1.05x slower                                                   |
| django_template            | 34.8 ms                                                    | 36.4 ms: 1.05x slower                                                   |
| pickle                     | 11.5 us                                                    | 12.0 us: 1.05x slower                                                   |
| regex_effbot               | 3.67 ms                                                    | 3.85 ms: 1.05x slower                                                   |
| tornado_http               | 94.6 ms                                                    | 99.4 ms: 1.05x slower                                                   |
| raytrace                   | 267 ms                                                     | 280 ms: 1.05x slower                                                    |
| sqlglot_parse              | 1.32 ms                                                    | 1.40 ms: 1.06x slower                                                   |
| sqlglot_optimize           | 55.5 ms                                                    | 58.8 ms: 1.06x slower                                                   |
| typing_runtime_protocols   | 165 us                                                     | 175 us: 1.06x slower                                                    |
| nqueens                    | 81.4 ms                                                    | 86.6 ms: 1.06x slower                                                   |
| sqlglot_transpile          | 1.63 ms                                                    | 1.74 ms: 1.06x slower                                                   |
| xml_etree_generate         | 87.4 ms                                                    | 93.2 ms: 1.07x slower                                                   |
| genshi_text                | 23.7 ms                                                    | 25.2 ms: 1.07x slower                                                   |
| pickle_list                | 5.11 us                                                    | 5.46 us: 1.07x slower                                                   |
| sympy_str                  | 282 ms                                                     | 304 ms: 1.08x slower                                                    |
| gunicorn                   | 1.28 ms                                                    | 1.38 ms: 1.08x slower                                                   |
| xml_etree_parse            | 162 ms                                                     | 174 ms: 1.08x slower                                                    |
| python_startup_no_site     | 7.11 ms                                                    | 7.68 ms: 1.08x slower                                                   |
| xml_etree_process          | 61.2 ms                                                    | 66.2 ms: 1.08x slower                                                   |
| sympy_expand               | 473 ms                                                     | 513 ms: 1.09x slower                                                    |
| gc_traversal               | 3.98 ms                                                    | 4.32 ms: 1.09x slower                                                   |
| aiohttp                    | 1.18 ms                                                    | 1.28 ms: 1.09x slower                                                   |
| pycparser                  | 1.16 sec                                                   | 1.26 sec: 1.09x slower                                                  |
| 2to3                       | 274 ms                                                     | 302 ms: 1.10x slower                                                    |
| async_generators           | 442 ms                                                     | 488 ms: 1.10x slower                                                    |
| sympy_integrate            | 20.5 ms                                                    | 22.8 ms: 1.11x slower                                                   |
| sympy_sum                  | 156 ms                                                     | 173 ms: 1.11x slower                                                    |
| html5lib                   | 67.2 ms                                                    | 75.0 ms: 1.12x slower                                                   |
| float                      | 78.9 ms                                                    | 89.8 ms: 1.14x slower                                                   |
| flaskblogging              | 9.01 ms                                                    | 10.4 ms: 1.16x slower                                                   |
| genshi_xml                 | 51.6 ms                                                    | 61.3 ms: 1.19x slower                                                   |
| dask                       | 369 ms                                                     | 449 ms: 1.21x slower                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 718 ms: 1.22x slower                                                    |
| create_gc_cycles           | 1.82 ms                                                    | 2.23 ms: 1.23x slower                                                   |
| deltablue                  | 3.25 ms                                                    | 3.99 ms: 1.23x slower                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 754 ms: 1.23x slower                                                    |
| async_tree_io              | 939 ms                                                     | 1.18 sec: 1.25x slower                                                  |
| async_tree_none            | 378 ms                                                     | 489 ms: 1.29x slower                                                    |
| async_tree_io_tg           | 936 ms                                                     | 1.21 sec: 1.29x slower                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 140 ms: 1.30x slower                                                    |
| pylint                     | 317 ms                                                     | 415 ms: 1.31x slower                                                    |
| async_tree_memoization_tg  | 444 ms                                                     | 588 ms: 1.33x slower                                                    |
| async_tree_memoization     | 463 ms                                                     | 618 ms: 1.33x slower                                                    |
| docutils                   | 2.83 sec                                                   | 3.83 sec: 1.36x slower                                                  |
| async_tree_none_tg         | 336 ms                                                     | 467 ms: 1.39x slower                                                    |
| telco                      | 8.41 ms                                                    | 170 ms: 20.25x slower                                                   |
| Geometric mean             | (ref)                                                      | 1.08x slower                                                            |

Benchmark hidden because not significant (3): logging_format, json, logging_simple
Ignored benchmarks (3) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, djangocms, mypy2

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.08x