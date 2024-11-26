# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a5
- machine: linux-x86_64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.318x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 377 ms: 1.41x slower                                       |
| chameleon      | 6.94 ms                                                | 12.3 ms: 1.77x slower                                      |
| docutils       | 2.59 sec                                               | 3.28 sec: 1.26x slower                                     |
| html5lib       | 64.2 ms                                                | 91.5 ms: 1.43x slower                                      |
| tornado_http   | 92.4 ms                                                | 137 ms: 1.49x slower                                       |
| Geometric mean | (ref)                                                  | 1.46x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_io_tg           | 857 ms                                                 | 839 ms: 1.02x faster                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 472 ms: 1.02x slower                                       |
| asyncio_websockets         | 552 ms                                                 | 567 ms: 1.03x slower                                       |
| async_tree_io              | 842 ms                                                 | 877 ms: 1.04x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 623 ms: 1.14x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 369 ms: 1.15x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 668 ms: 1.16x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 518 ms: 1.17x slower                                       |
| async_generators           | 436 ms                                                 | 511 ms: 1.17x slower                                       |
| async_tree_none            | 351 ms                                                 | 412 ms: 1.17x slower                                       |
| coroutines                 | 22.7 ms                                                | 29.3 ms: 1.29x slower                                      |
| Geometric mean             | (ref)                                                  | 1.12x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 192 ms: 1.03x slower                                       |
| float          | 79.2 ms                                                | 127 ms: 1.60x slower                                       |
| nbody          | 87.0 ms                                                | 215 ms: 2.47x slower                                       |
| Geometric mean | (ref)                                                  | 1.60x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.56 ms: 1.05x faster                                      |
| regex_v8       | 26.2 ms                                                | 26.9 ms: 1.03x slower                                      |
| regex_dna      | 218 ms                                                 | 230 ms: 1.05x slower                                       |
| regex_compile  | 132 ms                                                 | 204 ms: 1.55x slower                                       |
| Geometric mean | (ref)                                                  | 1.12x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 117 ms: 1.16x slower                                       |
| xml_etree_generate   | 86.7 ms                                                | 108 ms: 1.24x slower                                       |
| json_loads           | 27.2 us                                                | 34.8 us: 1.28x slower                                      |
| json_dumps           | 10.6 ms                                                | 13.7 ms: 1.30x slower                                      |
| xml_etree_process    | 60.6 ms                                                | 86.4 ms: 1.43x slower                                      |
| tomli_loads          | 2.14 sec                                               | 3.11 sec: 1.45x slower                                     |
| unpickle_pure_python | 216 us                                                 | 367 us: 1.70x slower                                       |
| pickle_pure_python   | 310 us                                                 | 528 us: 1.70x slower                                       |
| Geometric mean       | (ref)                                                  | 1.34x slower                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 13.6 ms: 1.09x slower                                      |
| python_startup_no_site | 6.96 ms                                                | 11.6 ms: 1.67x slower                                      |
| Geometric mean         | (ref)                                                  | 1.35x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_xml      | 50.9 ms                                                | 78.4 ms: 1.54x slower                                      |
| django_template | 35.2 ms                                                | 57.7 ms: 1.64x slower                                      |
| genshi_text     | 23.5 ms                                                | 38.9 ms: 1.65x slower                                      |
| mako            | 11.1 ms                                                | 21.0 ms: 1.90x slower                                      |
| Geometric mean  | (ref)                                                  | 1.68x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.08 ms: 2.22x faster                                      |
| gc_traversal               | 4.37 ms                                                | 2.57 ms: 1.70x faster                                      |
| regex_effbot               | 3.73 ms                                                | 3.56 ms: 1.05x faster                                      |
| async_tree_io_tg           | 857 ms                                                 | 839 ms: 1.02x faster                                       |
| typing_runtime_protocols   | 165 us                                                 | 167 us: 1.02x slower                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 472 ms: 1.02x slower                                       |
| regex_v8                   | 26.2 ms                                                | 26.9 ms: 1.03x slower                                      |
| asyncio_websockets         | 552 ms                                                 | 567 ms: 1.03x slower                                       |
| pidigits                   | 186 ms                                                 | 192 ms: 1.03x slower                                       |
| async_tree_io              | 842 ms                                                 | 877 ms: 1.04x slower                                       |
| regex_dna                  | 218 ms                                                 | 230 ms: 1.05x slower                                       |
| python_startup             | 12.5 ms                                                | 13.6 ms: 1.09x slower                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 623 ms: 1.14x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 369 ms: 1.15x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 668 ms: 1.16x slower                                       |
| xml_etree_iterparse        | 101 ms                                                 | 117 ms: 1.16x slower                                       |
| json                       | 5.36 ms                                                | 6.24 ms: 1.16x slower                                      |
| async_tree_memoization     | 442 ms                                                 | 518 ms: 1.17x slower                                       |
| async_generators           | 436 ms                                                 | 511 ms: 1.17x slower                                       |
| async_tree_none            | 351 ms                                                 | 412 ms: 1.17x slower                                       |
| mdp                        | 2.72 sec                                               | 3.30 sec: 1.21x slower                                     |
| xml_etree_generate         | 86.7 ms                                                | 108 ms: 1.24x slower                                       |
| meteor_contest             | 109 ms                                                 | 136 ms: 1.25x slower                                       |
| pylint                     | 313 ms                                                 | 390 ms: 1.25x slower                                       |
| generators                 | 29.0 ms                                                | 36.2 ms: 1.25x slower                                      |
| docutils                   | 2.59 sec                                               | 3.28 sec: 1.26x slower                                     |
| json_loads                 | 27.2 us                                                | 34.8 us: 1.28x slower                                      |
| coroutines                 | 22.7 ms                                                | 29.3 ms: 1.29x slower                                      |
| json_dumps                 | 10.6 ms                                                | 13.7 ms: 1.30x slower                                      |
| pycparser                  | 1.20 sec                                               | 1.57 sec: 1.31x slower                                     |
| scimark_fft                | 364 ms                                                 | 481 ms: 1.32x slower                                       |
| telco                      | 8.54 ms                                                | 11.7 ms: 1.37x slower                                      |
| fannkuch                   | 404 ms                                                 | 559 ms: 1.38x slower                                       |
| dulwich_log                | 64.3 ms                                                | 89.2 ms: 1.39x slower                                      |
| richards                   | 48.7 ms                                                | 68.0 ms: 1.40x slower                                      |
| 2to3                       | 267 ms                                                 | 377 ms: 1.41x slower                                       |
| nqueens                    | 78.4 ms                                                | 111 ms: 1.42x slower                                       |
| html5lib                   | 64.2 ms                                                | 91.5 ms: 1.43x slower                                      |
| xml_etree_process          | 60.6 ms                                                | 86.4 ms: 1.43x slower                                      |
| sympy_integrate            | 19.9 ms                                                | 28.4 ms: 1.43x slower                                      |
| crypto_pyaes               | 75.3 ms                                                | 108 ms: 1.44x slower                                       |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 7.26 ms: 1.44x slower                                      |
| tomli_loads                | 2.14 sec                                               | 3.11 sec: 1.45x slower                                     |
| deepcopy                   | 358 us                                                 | 527 us: 1.47x slower                                       |
| pathlib                    | 17.5 ms                                                | 25.9 ms: 1.48x slower                                      |
| deepcopy_reduce            | 3.20 us                                                | 4.74 us: 1.48x slower                                      |
| tornado_http               | 92.4 ms                                                | 137 ms: 1.49x slower                                       |
| richards_super             | 54.9 ms                                                | 82.3 ms: 1.50x slower                                      |
| sympy_str                  | 275 ms                                                 | 421 ms: 1.53x slower                                       |
| genshi_xml                 | 50.9 ms                                                | 78.4 ms: 1.54x slower                                      |
| pyflate                    | 471 ms                                                 | 728 ms: 1.55x slower                                       |
| regex_compile              | 132 ms                                                 | 204 ms: 1.55x slower                                       |
| deepcopy_memo              | 39.1 us                                                | 60.8 us: 1.55x slower                                      |
| comprehensions             | 16.5 us                                                | 25.7 us: 1.56x slower                                      |
| spectral_norm              | 115 ms                                                 | 181 ms: 1.57x slower                                       |
| sympy_expand               | 463 ms                                                 | 740 ms: 1.60x slower                                       |
| float                      | 79.2 ms                                                | 127 ms: 1.60x slower                                       |
| django_template            | 35.2 ms                                                | 57.7 ms: 1.64x slower                                      |
| sqlglot_normalize          | 108 ms                                                 | 177 ms: 1.65x slower                                       |
| pprint_safe_repr           | 728 ms                                                 | 1.20 sec: 1.65x slower                                     |
| sqlglot_optimize           | 53.7 ms                                                | 88.8 ms: 1.65x slower                                      |
| genshi_text                | 23.5 ms                                                | 38.9 ms: 1.65x slower                                      |
| python_startup_no_site     | 6.96 ms                                                | 11.6 ms: 1.67x slower                                      |
| pprint_pformat             | 1.49 sec                                               | 2.49 sec: 1.67x slower                                     |
| sympy_sum                  | 150 ms                                                 | 254 ms: 1.69x slower                                       |
| unpickle_pure_python       | 216 us                                                 | 367 us: 1.70x slower                                       |
| pickle_pure_python         | 310 us                                                 | 528 us: 1.70x slower                                       |
| logging_silent             | 102 ns                                                 | 176 ns: 1.73x slower                                       |
| logging_format             | 6.40 us                                                | 11.2 us: 1.75x slower                                      |
| chameleon                  | 6.94 ms                                                | 12.3 ms: 1.77x slower                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 119 ms: 1.77x slower                                       |
| logging_simple             | 5.72 us                                                | 10.2 us: 1.77x slower                                      |
| hexiom                     | 6.16 ms                                                | 11.0 ms: 1.79x slower                                      |
| sqlglot_transpile          | 1.58 ms                                                | 2.84 ms: 1.80x slower                                      |
| sqlglot_parse              | 1.27 ms                                                | 2.37 ms: 1.86x slower                                      |
| mako                       | 11.1 ms                                                | 21.0 ms: 1.90x slower                                      |
| go                         | 144 ms                                                 | 273 ms: 1.90x slower                                       |
| raytrace                   | 267 ms                                                 | 518 ms: 1.94x slower                                       |
| scimark_sor                | 124 ms                                                 | 241 ms: 1.95x slower                                       |
| chaos                      | 58.1 ms                                                | 115 ms: 1.98x slower                                       |
| scimark_lu                 | 113 ms                                                 | 250 ms: 2.22x slower                                       |
| deltablue                  | 3.23 ms                                                | 7.43 ms: 2.30x slower                                      |
| nbody                      | 87.0 ms                                                | 215 ms: 2.47x slower                                       |
| bench_thread_pool          | 822 us                                                 | 3.01 ms: 3.66x slower                                      |
| coverage                   | 84.0 ms                                                | 891 ms: 10.60x slower                                      |
| thrift                     | 809 us                                                 | 12.4 ms: 15.31x slower                                     |
| Geometric mean             | (ref)                                                  | 1.48x slower                                               |

Benchmark hidden because not significant (3): bench_mp_pool, xml_etree_parse, mypy2
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (11) of results/bm-20240312-3.13.0a5-076d169-NOGIL/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.318x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.36x
- 95% likely to have a slowdown of 1.33x
- 99% likely to have a slowdown of 1.30x

# Memory
- memory change: 1.00x