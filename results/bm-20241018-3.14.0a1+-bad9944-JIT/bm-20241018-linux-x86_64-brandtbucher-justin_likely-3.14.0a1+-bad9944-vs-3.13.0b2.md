# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_likely
- machine: linux-x86_64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.01x faster
- HPT reliability: 99.15%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 278 ms: 1.02x slower                                                  |
| docutils       | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                |
| html5lib       | 67.2 ms                                                    | 64.0 ms: 1.05x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 95.0 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 375 ms: 1.18x faster                                                  |
| async_tree_none            | 378 ms                                                     | 329 ms: 1.15x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 420 ms: 1.10x faster                                                  |
| async_tree_io              | 939 ms                                                     | 854 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 572 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 556 ms: 1.06x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 320 ms: 1.05x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 971 ms: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.08x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 84.5 ms: 1.05x faster                                                 |
| float          | 78.9 ms                                                    | 76.0 ms: 1.04x faster                                                 |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                      | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 216 ms: 1.02x faster                                                  |
| regex_v8       | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.68 ms: 1.00x slower                                                 |
| regex_compile  | 137 ms                                                     | 143 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|---------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate  | 87.4 ms                                                    | 78.8 ms: 1.11x faster                                                 |
| xml_etree_process   | 61.2 ms                                                    | 55.5 ms: 1.10x faster                                                 |
| tomli_loads         | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                |
| json_loads          | 28.9 us                                                    | 26.5 us: 1.09x faster                                                 |
| xml_etree_parse     | 162 ms                                                     | 149 ms: 1.09x faster                                                  |
| xml_etree_iterparse | 107 ms                                                     | 99.7 ms: 1.08x faster                                                 |
| unpickle            | 15.1 us                                                    | 14.3 us: 1.06x faster                                                 |
| pickle_list         | 5.11 us                                                    | 5.13 us: 1.00x slower                                                 |
| pickle_pure_python  | 305 us                                                     | 313 us: 1.02x slower                                                  |
| pickle              | 11.5 us                                                    | 11.9 us: 1.03x slower                                                 |
| unpickle_list       | 5.34 us                                                    | 5.53 us: 1.04x slower                                                 |
| json_dumps          | 10.7 ms                                                    | 11.2 ms: 1.04x slower                                                 |
| Geometric mean      | (ref)                                                      | 1.03x faster                                                          |

Benchmark hidden because not significant (2): pickle_dict, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                 |
| python_startup         | 10.8 ms                                                    | 11.9 ms: 1.11x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.1 ms: 1.11x faster                                                 |
| django_template | 34.8 ms                                                    | 36.7 ms: 1.05x slower                                                 |
| genshi_text     | 23.7 ms                                                    | 25.2 ms: 1.06x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 61.9 ms: 1.20x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.05x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 274 us: 1.34x faster                                                  |
| deepcopy_memo              | 39.7 us                                                    | 29.8 us: 1.33x faster                                                 |
| richards                   | 50.9 ms                                                    | 41.4 ms: 1.23x faster                                                 |
| richards_super             | 57.4 ms                                                    | 47.2 ms: 1.22x faster                                                 |
| scimark_fft                | 392 ms                                                     | 323 ms: 1.22x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 2.81 us: 1.19x faster                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 375 ms: 1.18x faster                                                  |
| async_tree_none            | 378 ms                                                     | 329 ms: 1.15x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 67.7 ms: 1.14x faster                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.44 sec: 1.13x faster                                                |
| mako                       | 11.2 ms                                                    | 10.1 ms: 1.11x faster                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 78.8 ms: 1.11x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 420 ms: 1.10x faster                                                  |
| xml_etree_process          | 61.2 ms                                                    | 55.5 ms: 1.10x faster                                                 |
| coverage                   | 93.1 ms                                                    | 84.6 ms: 1.10x faster                                                 |
| async_tree_io              | 939 ms                                                     | 854 ms: 1.10x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                |
| telco                      | 8.41 ms                                                    | 7.69 ms: 1.09x faster                                                 |
| json_loads                 | 28.9 us                                                    | 26.5 us: 1.09x faster                                                 |
| json                       | 5.31 ms                                                    | 4.88 ms: 1.09x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 149 ms: 1.09x faster                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.9 ms: 1.08x faster                                                 |
| scimark_sor                | 127 ms                                                     | 118 ms: 1.08x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.08x faster                                                  |
| go                         | 145 ms                                                     | 134 ms: 1.08x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 99.7 ms: 1.08x faster                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.90 ms: 1.08x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 572 ms: 1.07x faster                                                  |
| pyflate                    | 484 ms                                                     | 455 ms: 1.06x faster                                                  |
| sqlite_synth               | 2.99 us                                                    | 2.81 us: 1.06x faster                                                 |
| logging_silent             | 105 ns                                                     | 98.8 ns: 1.06x faster                                                 |
| logging_format             | 6.47 us                                                    | 6.11 us: 1.06x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 556 ms: 1.06x faster                                                  |
| unpickle                   | 15.1 us                                                    | 14.3 us: 1.06x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 320 ms: 1.05x faster                                                  |
| html5lib                   | 67.2 ms                                                    | 64.0 ms: 1.05x faster                                                 |
| nbody                      | 88.3 ms                                                    | 84.5 ms: 1.05x faster                                                 |
| float                      | 78.9 ms                                                    | 76.0 ms: 1.04x faster                                                 |
| thrift                     | 823 us                                                     | 794 us: 1.04x faster                                                  |
| chaos                      | 61.3 ms                                                    | 59.4 ms: 1.03x faster                                                 |
| spectral_norm              | 116 ms                                                     | 113 ms: 1.03x faster                                                  |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| logging_simple             | 5.74 us                                                    | 5.62 us: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                                  |
| regex_dna                  | 221 ms                                                     | 216 ms: 1.02x faster                                                  |
| pprint_safe_repr           | 758 ms                                                     | 742 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                |
| asyncio_tcp                | 508 ms                                                     | 499 ms: 1.02x faster                                                  |
| regex_v8                   | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                                 |
| coroutines                 | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                 |
| mdp                        | 2.79 sec                                                   | 2.75 sec: 1.01x faster                                                |
| meteor_contest             | 110 ms                                                     | 109 ms: 1.01x faster                                                  |
| dulwich_log                | 67.2 ms                                                    | 66.7 ms: 1.01x faster                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.68 ms: 1.00x slower                                                 |
| tornado_http               | 94.6 ms                                                    | 95.0 ms: 1.00x slower                                                 |
| pickle_list                | 5.11 us                                                    | 5.13 us: 1.00x slower                                                 |
| typing_runtime_protocols   | 165 us                                                     | 166 us: 1.01x slower                                                  |
| pycparser                  | 1.16 sec                                                   | 1.17 sec: 1.01x slower                                                |
| sqlglot_parse              | 1.32 ms                                                    | 1.34 ms: 1.01x slower                                                 |
| 2to3                       | 274 ms                                                     | 278 ms: 1.02x slower                                                  |
| pickle_pure_python         | 305 us                                                     | 313 us: 1.02x slower                                                  |
| async_generators           | 442 ms                                                     | 454 ms: 1.03x slower                                                  |
| docutils                   | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                |
| pickle                     | 11.5 us                                                    | 11.9 us: 1.03x slower                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 1.69 ms: 1.03x slower                                                 |
| unpickle_list              | 5.34 us                                                    | 5.53 us: 1.04x slower                                                 |
| async_tree_io_tg           | 936 ms                                                     | 971 ms: 1.04x slower                                                  |
| sqlglot_normalize          | 110 ms                                                     | 115 ms: 1.04x slower                                                  |
| regex_compile              | 137 ms                                                     | 143 ms: 1.04x slower                                                  |
| raytrace                   | 267 ms                                                     | 278 ms: 1.04x slower                                                  |
| json_dumps                 | 10.7 ms                                                    | 11.2 ms: 1.04x slower                                                 |
| comprehensions             | 16.6 us                                                    | 17.4 us: 1.05x slower                                                 |
| bench_thread_pool          | 834 us                                                     | 878 us: 1.05x slower                                                  |
| django_template            | 34.8 ms                                                    | 36.7 ms: 1.05x slower                                                 |
| genshi_text                | 23.7 ms                                                    | 25.2 ms: 1.06x slower                                                 |
| sympy_expand               | 473 ms                                                     | 505 ms: 1.07x slower                                                  |
| sympy_str                  | 282 ms                                                     | 303 ms: 1.07x slower                                                  |
| nqueens                    | 81.4 ms                                                    | 88.6 ms: 1.09x slower                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 60.6 ms: 1.09x slower                                                 |
| python_startup             | 10.8 ms                                                    | 11.9 ms: 1.11x slower                                                 |
| hexiom                     | 6.30 ms                                                    | 7.07 ms: 1.12x slower                                                 |
| sympy_sum                  | 156 ms                                                     | 175 ms: 1.13x slower                                                  |
| gc_traversal               | 3.98 ms                                                    | 4.52 ms: 1.14x slower                                                 |
| sympy_integrate            | 20.5 ms                                                    | 23.6 ms: 1.15x slower                                                 |
| generators                 | 29.6 ms                                                    | 35.2 ms: 1.19x slower                                                 |
| pylint                     | 317 ms                                                     | 377 ms: 1.19x slower                                                  |
| genshi_xml                 | 51.6 ms                                                    | 61.9 ms: 1.20x slower                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 2.68 ms: 1.48x slower                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 84.0 ms: 3.52x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (5): fannkuch, pprint_pformat, pickle_dict, unpickle_pure_python, deltablue
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 99.15% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.19x