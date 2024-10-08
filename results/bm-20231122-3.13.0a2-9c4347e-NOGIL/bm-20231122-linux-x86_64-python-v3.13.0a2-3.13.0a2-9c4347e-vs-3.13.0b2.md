# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.23x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 0.57x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 294 ms: 1.07x slower                                       |
| chameleon      | 7.22 ms                                                    | 7.76 ms: 1.07x slower                                      |
| docutils       | 2.83 sec                                                   | 2.89 sec: 1.02x slower                                     |
| html5lib       | 67.2 ms                                                    | 71.7 ms: 1.07x slower                                      |
| tornado_http   | 94.6 ms                                                    | 108 ms: 1.14x slower                                       |
| Geometric mean | (ref)                                                      | 1.07x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 611 ms                                                     | 804 ms: 1.32x slower                                       |
| async_tree_none            | 378 ms                                                     | 509 ms: 1.35x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 657 ms: 1.42x slower                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 850 ms: 1.45x slower                                       |
| async_tree_io              | 939 ms                                                     | 1.39 sec: 1.48x slower                                     |
| async_tree_io_tg           | 936 ms                                                     | 1.45 sec: 1.55x slower                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 692 ms: 1.56x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 540 ms: 1.61x slower                                       |
| Geometric mean             | (ref)                                                      | 1.46x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 194 ms: 1.01x slower                                       |
| float          | 78.9 ms                                                    | 95.5 ms: 1.21x slower                                      |
| nbody          | 88.3 ms                                                    | 110 ms: 1.24x slower                                       |
| Geometric mean | (ref)                                                      | 1.15x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 222 ms: 1.00x slower                                       |
| regex_v8       | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                      |
| regex_effbot   | 3.67 ms                                                    | 3.83 ms: 1.04x slower                                      |
| regex_compile  | 137 ms                                                     | 149 ms: 1.09x slower                                       |
| Geometric mean | (ref)                                                      | 1.04x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_list          | 5.11 us                                                    | 4.71 us: 1.08x faster                                      |
| pickle_dict          | 34.8 us                                                    | 32.7 us: 1.06x faster                                      |
| unpickle_list        | 5.34 us                                                    | 5.26 us: 1.02x faster                                      |
| pickle               | 11.5 us                                                    | 11.4 us: 1.01x faster                                      |
| unpickle             | 15.1 us                                                    | 15.4 us: 1.02x slower                                      |
| json_dumps           | 10.7 ms                                                    | 11.3 ms: 1.05x slower                                      |
| xml_etree_iterparse  | 107 ms                                                     | 114 ms: 1.06x slower                                       |
| json_loads           | 28.9 us                                                    | 30.9 us: 1.07x slower                                      |
| pickle_pure_python   | 305 us                                                     | 335 us: 1.10x slower                                       |
| tomli_loads          | 2.12 sec                                                   | 2.37 sec: 1.12x slower                                     |
| unpickle_pure_python | 218 us                                                     | 246 us: 1.13x slower                                       |
| xml_etree_parse      | 162 ms                                                     | 472 ms: 2.92x slower                                       |
| xml_etree_process    | 61.2 ms                                                    | 1.03 sec: 16.81x slower                                    |
| xml_etree_generate   | 87.4 ms                                                    | 1.58 sec: 18.09x slower                                    |
| Geometric mean       | (ref)                                                      | 1.67x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.1 ms: 1.04x slower                                      |
| python_startup_no_site | 7.11 ms                                                    | 9.60 ms: 1.35x slower                                      |
| Geometric mean         | (ref)                                                      | 1.18x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 24.9 ms: 1.05x slower                                      |
| genshi_xml      | 51.6 ms                                                    | 56.2 ms: 1.09x slower                                      |
| django_template | 34.8 ms                                                    | 38.3 ms: 1.10x slower                                      |
| mako            | 11.2 ms                                                    | 12.9 ms: 1.15x slower                                      |
| Geometric mean  | (ref)                                                      | 1.10x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 1.82 ms                                                    | 1.22 ms: 1.49x faster                                      |
| typing_runtime_protocols   | 165 us                                                     | 127 us: 1.30x faster                                       |
| gc_traversal               | 3.98 ms                                                    | 3.64 ms: 1.09x faster                                      |
| pickle_list                | 5.11 us                                                    | 4.71 us: 1.08x faster                                      |
| pickle_dict                | 34.8 us                                                    | 32.7 us: 1.06x faster                                      |
| bench_mp_pool              | 23.9 ms                                                    | 22.6 ms: 1.06x faster                                      |
| unpickle_list              | 5.34 us                                                    | 5.26 us: 1.02x faster                                      |
| pickle                     | 11.5 us                                                    | 11.4 us: 1.01x faster                                      |
| asyncio_websockets         | 567 ms                                                     | 564 ms: 1.00x faster                                       |
| regex_dna                  | 221 ms                                                     | 222 ms: 1.00x slower                                       |
| asyncio_tcp                | 508 ms                                                     | 511 ms: 1.01x slower                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.85 sec: 1.01x slower                                     |
| pidigits                   | 191 ms                                                     | 194 ms: 1.01x slower                                       |
| unpickle                   | 15.1 us                                                    | 15.4 us: 1.02x slower                                      |
| richards                   | 50.9 ms                                                    | 51.9 ms: 1.02x slower                                      |
| docutils                   | 2.83 sec                                                   | 2.89 sec: 1.02x slower                                     |
| richards_super             | 57.4 ms                                                    | 59.1 ms: 1.03x slower                                      |
| regex_v8                   | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                      |
| scimark_fft                | 392 ms                                                     | 405 ms: 1.03x slower                                       |
| crypto_pyaes               | 77.5 ms                                                    | 80.1 ms: 1.03x slower                                      |
| python_startup             | 10.8 ms                                                    | 11.1 ms: 1.04x slower                                      |
| mdp                        | 2.79 sec                                                   | 2.89 sec: 1.04x slower                                     |
| scimark_lu                 | 122 ms                                                     | 126 ms: 1.04x slower                                       |
| regex_effbot               | 3.67 ms                                                    | 3.83 ms: 1.04x slower                                      |
| json_dumps                 | 10.7 ms                                                    | 11.3 ms: 1.05x slower                                      |
| genshi_text                | 23.7 ms                                                    | 24.9 ms: 1.05x slower                                      |
| pyflate                    | 484 ms                                                     | 510 ms: 1.05x slower                                       |
| gunicorn                   | 1.28 ms                                                    | 1.35 ms: 1.05x slower                                      |
| generators                 | 29.6 ms                                                    | 31.2 ms: 1.05x slower                                      |
| dulwich_log                | 67.2 ms                                                    | 70.8 ms: 1.05x slower                                      |
| deepcopy_reduce            | 3.35 us                                                    | 3.53 us: 1.05x slower                                      |
| aiohttp                    | 1.18 ms                                                    | 1.25 ms: 1.06x slower                                      |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.61 ms: 1.06x slower                                      |
| xml_etree_iterparse        | 107 ms                                                     | 114 ms: 1.06x slower                                       |
| meteor_contest             | 110 ms                                                     | 117 ms: 1.06x slower                                       |
| html5lib                   | 67.2 ms                                                    | 71.7 ms: 1.07x slower                                      |
| deepcopy                   | 367 us                                                     | 392 us: 1.07x slower                                       |
| pprint_pformat             | 1.56 sec                                                   | 1.66 sec: 1.07x slower                                     |
| coroutines                 | 23.2 ms                                                    | 24.8 ms: 1.07x slower                                      |
| sqlglot_optimize           | 55.5 ms                                                    | 59.4 ms: 1.07x slower                                      |
| sqlglot_normalize          | 110 ms                                                     | 118 ms: 1.07x slower                                       |
| json                       | 5.31 ms                                                    | 5.68 ms: 1.07x slower                                      |
| json_loads                 | 28.9 us                                                    | 30.9 us: 1.07x slower                                      |
| pprint_safe_repr           | 758 ms                                                     | 812 ms: 1.07x slower                                       |
| 2to3                       | 274 ms                                                     | 294 ms: 1.07x slower                                       |
| chameleon                  | 7.22 ms                                                    | 7.76 ms: 1.07x slower                                      |
| pylint                     | 317 ms                                                     | 341 ms: 1.08x slower                                       |
| sqlite_synth               | 2.99 us                                                    | 3.23 us: 1.08x slower                                      |
| deepcopy_memo              | 39.7 us                                                    | 43.0 us: 1.08x slower                                      |
| go                         | 145 ms                                                     | 157 ms: 1.08x slower                                       |
| nqueens                    | 81.4 ms                                                    | 88.6 ms: 1.09x slower                                      |
| genshi_xml                 | 51.6 ms                                                    | 56.2 ms: 1.09x slower                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.44 ms: 1.09x slower                                      |
| hexiom                     | 6.30 ms                                                    | 6.86 ms: 1.09x slower                                      |
| regex_compile              | 137 ms                                                     | 149 ms: 1.09x slower                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.79 ms: 1.10x slower                                      |
| logging_format             | 6.47 us                                                    | 7.09 us: 1.10x slower                                      |
| scimark_sor                | 127 ms                                                     | 140 ms: 1.10x slower                                       |
| pickle_pure_python         | 305 us                                                     | 335 us: 1.10x slower                                       |
| scimark_monte_carlo        | 69.2 ms                                                    | 76.1 ms: 1.10x slower                                      |
| pycparser                  | 1.16 sec                                                   | 1.27 sec: 1.10x slower                                     |
| django_template            | 34.8 ms                                                    | 38.3 ms: 1.10x slower                                      |
| logging_silent             | 105 ns                                                     | 116 ns: 1.11x slower                                       |
| comprehensions             | 16.6 us                                                    | 18.5 us: 1.11x slower                                      |
| tomli_loads                | 2.12 sec                                                   | 2.37 sec: 1.12x slower                                     |
| spectral_norm              | 116 ms                                                     | 130 ms: 1.12x slower                                       |
| sympy_integrate            | 20.5 ms                                                    | 22.9 ms: 1.12x slower                                      |
| chaos                      | 61.3 ms                                                    | 68.7 ms: 1.12x slower                                      |
| logging_simple             | 5.74 us                                                    | 6.44 us: 1.12x slower                                      |
| fannkuch                   | 402 ms                                                     | 451 ms: 1.12x slower                                       |
| unpickle_pure_python       | 218 us                                                     | 246 us: 1.13x slower                                       |
| flaskblogging              | 9.01 ms                                                    | 10.2 ms: 1.13x slower                                      |
| async_generators           | 442 ms                                                     | 500 ms: 1.13x slower                                       |
| tornado_http               | 94.6 ms                                                    | 108 ms: 1.14x slower                                       |
| telco                      | 8.41 ms                                                    | 9.60 ms: 1.14x slower                                      |
| pathlib                    | 17.3 ms                                                    | 19.8 ms: 1.14x slower                                      |
| mako                       | 11.2 ms                                                    | 12.9 ms: 1.15x slower                                      |
| raytrace                   | 267 ms                                                     | 314 ms: 1.18x slower                                       |
| sympy_str                  | 282 ms                                                     | 332 ms: 1.18x slower                                       |
| float                      | 78.9 ms                                                    | 95.5 ms: 1.21x slower                                      |
| deltablue                  | 3.25 ms                                                    | 3.99 ms: 1.23x slower                                      |
| nbody                      | 88.3 ms                                                    | 110 ms: 1.24x slower                                       |
| sympy_expand               | 473 ms                                                     | 613 ms: 1.30x slower                                       |
| bench_thread_pool          | 834 us                                                     | 1.09 ms: 1.30x slower                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 804 ms: 1.32x slower                                       |
| async_tree_none            | 378 ms                                                     | 509 ms: 1.35x slower                                       |
| python_startup_no_site     | 7.11 ms                                                    | 9.60 ms: 1.35x slower                                      |
| sympy_sum                  | 156 ms                                                     | 211 ms: 1.35x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 657 ms: 1.42x slower                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 850 ms: 1.45x slower                                       |
| async_tree_io              | 939 ms                                                     | 1.39 sec: 1.48x slower                                     |
| mypy2                      | 742 ms                                                     | 1.15 sec: 1.55x slower                                     |
| async_tree_io_tg           | 936 ms                                                     | 1.45 sec: 1.55x slower                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 692 ms: 1.56x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 540 ms: 1.61x slower                                       |
| xml_etree_parse            | 162 ms                                                     | 472 ms: 2.92x slower                                       |
| coverage                   | 93.1 ms                                                    | 725 ms: 7.79x slower                                       |
| thrift                     | 823 us                                                     | 9.50 ms: 11.55x slower                                     |
| xml_etree_process          | 61.2 ms                                                    | 1.03 sec: 16.81x slower                                    |
| xml_etree_generate         | 87.4 ms                                                    | 1.58 sec: 18.09x slower                                    |
| Geometric mean             | (ref)                                                      | 1.23x slower                                               |
Ignored benchmarks (3) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, dask, djangocms

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 0.57x