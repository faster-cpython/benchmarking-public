# Results vs. 3.13.0

- fork: python
- ref: 33eeccf6d4f16e483b4c
- machine: linux-x86_64
- commit hash: 33eeccf
- commit date: 2024-09-17
- overall geometric mean: 1.029x faster
- HPT reliability: 85.17%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 276 ms: 1.04x slower                                                  |
| docutils       | 2.59 sec                                               | 2.96 sec: 1.14x slower                                                |
| html5lib       | 64.2 ms                                                | 65.1 ms: 1.01x slower                                                 |
| tornado_http   | 92.4 ms                                                | 94.4 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 387 ms: 1.20x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 399 ms: 1.11x faster                                                  |
| async_tree_none            | 351 ms                                                 | 316 ms: 1.11x faster                                                  |
| async_tree_none_tg         | 321 ms                                                 | 306 ms: 1.05x faster                                                  |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 557 ms: 1.02x slower                                                  |
| async_generators           | 436 ms                                                 | 451 ms: 1.03x slower                                                  |
| coroutines                 | 22.7 ms                                                | 23.6 ms: 1.04x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 69.9 ms: 1.13x faster                                                 |
| nbody          | 87.0 ms                                                | 79.7 ms: 1.09x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.6 ms: 1.06x faster                                                 |
| regex_effbot   | 3.73 ms                                                | 3.82 ms: 1.03x slower                                                 |
| regex_dna      | 218 ms                                                 | 224 ms: 1.03x slower                                                  |
| regex_compile  | 132 ms                                                 | 142 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process   | 60.6 ms                                                | 54.1 ms: 1.12x faster                                                 |
| xml_etree_generate  | 86.7 ms                                                | 77.8 ms: 1.11x faster                                                 |
| tomli_loads         | 2.14 sec                                               | 1.95 sec: 1.10x faster                                                |
| xml_etree_parse     | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| json_dumps          | 10.6 ms                                                | 10.1 ms: 1.04x faster                                                 |
| xml_etree_iterparse | 101 ms                                                 | 98.2 ms: 1.03x faster                                                 |
| json_loads          | 27.2 us                                                | 26.9 us: 1.01x faster                                                 |
| pickle_pure_python  | 310 us                                                 | 307 us: 1.01x faster                                                  |
| Geometric mean      | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                 |
| python_startup_no_site | 6.96 ms                                                | 7.09 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                 |
| django_template | 35.2 ms                                                | 36.1 ms: 1.03x slower                                                 |
| genshi_text     | 23.5 ms                                                | 25.5 ms: 1.08x slower                                                 |
| genshi_xml      | 50.9 ms                                                | 59.6 ms: 1.17x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 27.0 us: 1.45x faster                                                 |
| create_gc_cycles           | 2.41 ms                                                | 1.76 ms: 1.37x faster                                                 |
| deepcopy                   | 358 us                                                 | 263 us: 1.36x faster                                                  |
| richards                   | 48.7 ms                                                | 39.7 ms: 1.23x faster                                                 |
| richards_super             | 54.9 ms                                                | 45.7 ms: 1.20x faster                                                 |
| deepcopy_reduce            | 3.20 us                                                | 2.67 us: 1.20x faster                                                 |
| async_tree_memoization_tg  | 464 ms                                                 | 387 ms: 1.20x faster                                                  |
| python_startup             | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                 |
| scimark_fft                | 364 ms                                                 | 312 ms: 1.17x faster                                                  |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.39 ms: 1.15x faster                                                 |
| crypto_pyaes               | 75.3 ms                                                | 66.2 ms: 1.14x faster                                                 |
| float                      | 79.2 ms                                                | 69.9 ms: 1.13x faster                                                 |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                  |
| gc_traversal               | 4.37 ms                                                | 3.90 ms: 1.12x faster                                                 |
| xml_etree_process          | 60.6 ms                                                | 54.1 ms: 1.12x faster                                                 |
| xml_etree_generate         | 86.7 ms                                                | 77.8 ms: 1.11x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 399 ms: 1.11x faster                                                  |
| async_tree_none            | 351 ms                                                 | 316 ms: 1.11x faster                                                  |
| mako                       | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                 |
| go                         | 144 ms                                                 | 130 ms: 1.10x faster                                                  |
| tomli_loads                | 2.14 sec                                               | 1.95 sec: 1.10x faster                                                |
| nbody                      | 87.0 ms                                                | 79.7 ms: 1.09x faster                                                 |
| fannkuch                   | 404 ms                                                 | 373 ms: 1.08x faster                                                  |
| pathlib                    | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                 |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| json                       | 5.36 ms                                                | 5.02 ms: 1.07x faster                                                 |
| telco                      | 8.54 ms                                                | 8.01 ms: 1.07x faster                                                 |
| bpe_tokeniser              | 4.75 sec                                               | 4.45 sec: 1.07x faster                                                |
| regex_v8                   | 26.2 ms                                                | 24.6 ms: 1.06x faster                                                 |
| scimark_sor                | 124 ms                                                 | 116 ms: 1.06x faster                                                  |
| scimark_monte_carlo        | 67.4 ms                                                | 63.5 ms: 1.06x faster                                                 |
| pyflate                    | 471 ms                                                 | 448 ms: 1.05x faster                                                  |
| logging_format             | 6.40 us                                                | 6.10 us: 1.05x faster                                                 |
| async_tree_none_tg         | 321 ms                                                 | 306 ms: 1.05x faster                                                  |
| json_dumps                 | 10.6 ms                                                | 10.1 ms: 1.04x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                |
| thrift                     | 809 us                                                 | 781 us: 1.04x faster                                                  |
| scimark_lu                 | 113 ms                                                 | 109 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                                 |
| logging_simple             | 5.72 us                                                | 5.57 us: 1.03x faster                                                 |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.02x faster                                                  |
| mdp                        | 2.72 sec                                               | 2.66 sec: 1.02x faster                                                |
| json_loads                 | 27.2 us                                                | 26.9 us: 1.01x faster                                                 |
| pickle_pure_python         | 310 us                                                 | 307 us: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| deltablue                  | 3.23 ms                                                | 3.21 ms: 1.00x faster                                                 |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                  |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                                 |
| chaos                      | 58.1 ms                                                | 58.8 ms: 1.01x slower                                                 |
| html5lib                   | 64.2 ms                                                | 65.1 ms: 1.01x slower                                                 |
| coverage                   | 84.0 ms                                                | 85.2 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.96 ms                                                | 7.09 ms: 1.02x slower                                                 |
| bench_thread_pool          | 822 us                                                 | 837 us: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 557 ms: 1.02x slower                                                  |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                  |
| tornado_http               | 92.4 ms                                                | 94.4 ms: 1.02x slower                                                 |
| regex_effbot               | 3.73 ms                                                | 3.82 ms: 1.03x slower                                                 |
| regex_dna                  | 218 ms                                                 | 224 ms: 1.03x slower                                                  |
| django_template            | 35.2 ms                                                | 36.1 ms: 1.03x slower                                                 |
| raytrace                   | 267 ms                                                 | 276 ms: 1.03x slower                                                  |
| pprint_safe_repr           | 728 ms                                                 | 753 ms: 1.03x slower                                                  |
| async_generators           | 436 ms                                                 | 451 ms: 1.03x slower                                                  |
| 2to3                       | 267 ms                                                 | 276 ms: 1.04x slower                                                  |
| coroutines                 | 22.7 ms                                                | 23.6 ms: 1.04x slower                                                 |
| pprint_pformat             | 1.49 sec                                               | 1.57 sec: 1.05x slower                                                |
| dulwich_log                | 64.3 ms                                                | 67.6 ms: 1.05x slower                                                 |
| sqlglot_normalize          | 108 ms                                                 | 113 ms: 1.05x slower                                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.06x slower                                                 |
| sqlglot_transpile          | 1.58 ms                                                | 1.69 ms: 1.07x slower                                                 |
| nqueens                    | 78.4 ms                                                | 83.9 ms: 1.07x slower                                                 |
| regex_compile              | 132 ms                                                 | 142 ms: 1.07x slower                                                  |
| sqlglot_optimize           | 53.7 ms                                                | 58.0 ms: 1.08x slower                                                 |
| genshi_text                | 23.5 ms                                                | 25.5 ms: 1.08x slower                                                 |
| sympy_expand               | 463 ms                                                 | 503 ms: 1.09x slower                                                  |
| sympy_str                  | 275 ms                                                 | 299 ms: 1.09x slower                                                  |
| hexiom                     | 6.16 ms                                                | 6.88 ms: 1.12x slower                                                 |
| generators                 | 29.0 ms                                                | 32.7 ms: 1.13x slower                                                 |
| docutils                   | 2.59 sec                                               | 2.96 sec: 1.14x slower                                                |
| sympy_integrate            | 19.9 ms                                                | 22.8 ms: 1.14x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 172 ms: 1.15x slower                                                  |
| genshi_xml                 | 50.9 ms                                                | 59.6 ms: 1.17x slower                                                 |
| pylint                     | 313 ms                                                 | 372 ms: 1.19x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (6): typing_runtime_protocols, async_tree_cpu_io_mixed, unpickle_pure_python, bench_mp_pool, async_tree_io_tg, async_tree_io
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240917-3.14.0a0-33eeccf-JIT/bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.029x faster
# HPT report

- Reliability score: 85.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x