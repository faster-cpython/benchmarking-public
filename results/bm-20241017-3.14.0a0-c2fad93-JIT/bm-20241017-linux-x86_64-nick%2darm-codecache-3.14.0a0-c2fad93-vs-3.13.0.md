# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.012x faster
- HPT reliability: 56.70%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 278 ms: 1.04x slower                                           |
| docutils       | 2.59 sec                                               | 2.96 sec: 1.14x slower                                         |
| sphinx         | 1.03 sec                                               | 1.16 sec: 1.12x slower                                         |
| tornado_http   | 92.4 ms                                                | 94.9 ms: 1.03x slower                                          |
| Geometric mean | (ref)                                                  | 1.07x slower                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 388 ms: 1.20x faster                                           |
| async_tree_none            | 351 ms                                                 | 331 ms: 1.06x faster                                           |
| async_tree_none_tg         | 321 ms                                                 | 307 ms: 1.04x faster                                           |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 555 ms: 1.04x faster                                           |
| asyncio_websockets         | 552 ms                                                 | 559 ms: 1.01x slower                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 561 ms: 1.03x slower                                           |
| async_tree_io_tg           | 857 ms                                                 | 890 ms: 1.04x slower                                           |
| async_generators           | 436 ms                                                 | 463 ms: 1.06x slower                                           |
| async_tree_io              | 842 ms                                                 | 897 ms: 1.07x slower                                           |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (2): async_tree_memoization, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 79.3 ms: 1.10x faster                                          |
| float          | 79.2 ms                                                | 74.3 ms: 1.07x faster                                          |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                           |
| Geometric mean | (ref)                                                  | 1.05x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 26.8 ms: 1.02x slower                                          |
| regex_effbot   | 3.73 ms                                                | 3.81 ms: 1.02x slower                                          |
| regex_compile  | 132 ms                                                 | 138 ms: 1.05x slower                                           |
| regex_dna      | 218 ms                                                 | 229 ms: 1.05x slower                                           |
| Geometric mean | (ref)                                                  | 1.03x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|---------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads         | 2.14 sec                                               | 1.93 sec: 1.11x faster                                         |
| xml_etree_process   | 60.6 ms                                                | 54.8 ms: 1.11x faster                                          |
| xml_etree_generate  | 86.7 ms                                                | 78.6 ms: 1.10x faster                                          |
| xml_etree_parse     | 156 ms                                                 | 147 ms: 1.06x faster                                           |
| json_dumps          | 10.6 ms                                                | 10.1 ms: 1.04x faster                                          |
| pickle_pure_python  | 310 us                                                 | 304 us: 1.02x faster                                           |
| xml_etree_iterparse | 101 ms                                                 | 99.5 ms: 1.02x faster                                          |
| json_loads          | 27.2 us                                                | 26.8 us: 1.02x faster                                          |
| Geometric mean      | (ref)                                                  | 1.05x faster                                                   |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.9 ms: 1.05x faster                                          |
| python_startup_no_site | 6.96 ms                                                | 7.07 ms: 1.02x slower                                          |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.87 ms: 1.12x faster                                          |
| django_template | 35.2 ms                                                | 36.7 ms: 1.04x slower                                          |
| genshi_text     | 23.5 ms                                                | 25.0 ms: 1.06x slower                                          |
| genshi_xml      | 50.9 ms                                                | 59.7 ms: 1.17x slower                                          |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 26.8 us: 1.46x faster                                          |
| deepcopy                   | 358 us                                                 | 262 us: 1.37x faster                                           |
| deepcopy_reduce            | 3.20 us                                                | 2.64 us: 1.21x faster                                          |
| scimark_fft                | 364 ms                                                 | 303 ms: 1.20x faster                                           |
| async_tree_memoization_tg  | 464 ms                                                 | 388 ms: 1.20x faster                                           |
| richards_super             | 54.9 ms                                                | 46.9 ms: 1.17x faster                                          |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.40 ms: 1.15x faster                                          |
| richards                   | 48.7 ms                                                | 42.6 ms: 1.14x faster                                          |
| crypto_pyaes               | 75.3 ms                                                | 67.0 ms: 1.12x faster                                          |
| mako                       | 11.1 ms                                                | 9.87 ms: 1.12x faster                                          |
| telco                      | 8.54 ms                                                | 7.64 ms: 1.12x faster                                          |
| tomli_loads                | 2.14 sec                                               | 1.93 sec: 1.11x faster                                         |
| pathlib                    | 17.5 ms                                                | 15.8 ms: 1.11x faster                                          |
| xml_etree_process          | 60.6 ms                                                | 54.8 ms: 1.11x faster                                          |
| xml_etree_generate         | 86.7 ms                                                | 78.6 ms: 1.10x faster                                          |
| nbody                      | 87.0 ms                                                | 79.3 ms: 1.10x faster                                          |
| go                         | 144 ms                                                 | 132 ms: 1.09x faster                                           |
| scimark_monte_carlo        | 67.4 ms                                                | 62.8 ms: 1.07x faster                                          |
| mdp                        | 2.72 sec                                               | 2.54 sec: 1.07x faster                                         |
| float                      | 79.2 ms                                                | 74.3 ms: 1.07x faster                                          |
| async_tree_none            | 351 ms                                                 | 331 ms: 1.06x faster                                           |
| logging_silent             | 102 ns                                                 | 96.0 ns: 1.06x faster                                          |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                           |
| json                       | 5.36 ms                                                | 5.06 ms: 1.06x faster                                          |
| bpe_tokeniser              | 4.75 sec                                               | 4.51 sec: 1.05x faster                                         |
| python_startup             | 12.5 ms                                                | 11.9 ms: 1.05x faster                                          |
| fannkuch                   | 404 ms                                                 | 385 ms: 1.05x faster                                           |
| pprint_safe_repr           | 728 ms                                                 | 697 ms: 1.04x faster                                           |
| async_tree_none_tg         | 321 ms                                                 | 307 ms: 1.04x faster                                           |
| logging_format             | 6.40 us                                                | 6.14 us: 1.04x faster                                          |
| json_dumps                 | 10.6 ms                                                | 10.1 ms: 1.04x faster                                          |
| pyflate                    | 471 ms                                                 | 453 ms: 1.04x faster                                           |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 555 ms: 1.04x faster                                           |
| thrift                     | 809 us                                                 | 780 us: 1.04x faster                                           |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                           |
| scimark_lu                 | 113 ms                                                 | 109 ms: 1.03x faster                                           |
| logging_simple             | 5.72 us                                                | 5.58 us: 1.02x faster                                          |
| pickle_pure_python         | 310 us                                                 | 304 us: 1.02x faster                                           |
| gc_traversal               | 4.37 ms                                                | 4.29 ms: 1.02x faster                                          |
| xml_etree_iterparse        | 101 ms                                                 | 99.5 ms: 1.02x faster                                          |
| json_loads                 | 27.2 us                                                | 26.8 us: 1.02x faster                                          |
| pprint_pformat             | 1.49 sec                                               | 1.47 sec: 1.01x faster                                         |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                           |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                           |
| typing_runtime_protocols   | 165 us                                                 | 166 us: 1.01x slower                                           |
| coverage                   | 84.0 ms                                                | 84.9 ms: 1.01x slower                                          |
| asyncio_websockets         | 552 ms                                                 | 559 ms: 1.01x slower                                           |
| pycparser                  | 1.20 sec                                               | 1.22 sec: 1.01x slower                                         |
| python_startup_no_site     | 6.96 ms                                                | 7.07 ms: 1.02x slower                                          |
| regex_v8                   | 26.2 ms                                                | 26.8 ms: 1.02x slower                                          |
| regex_effbot               | 3.73 ms                                                | 3.81 ms: 1.02x slower                                          |
| chaos                      | 58.1 ms                                                | 59.5 ms: 1.02x slower                                          |
| tornado_http               | 92.4 ms                                                | 94.9 ms: 1.03x slower                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 561 ms: 1.03x slower                                           |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                          |
| raytrace                   | 267 ms                                                 | 277 ms: 1.04x slower                                           |
| async_tree_io_tg           | 857 ms                                                 | 890 ms: 1.04x slower                                           |
| dulwich_log                | 64.3 ms                                                | 66.9 ms: 1.04x slower                                          |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                          |
| django_template            | 35.2 ms                                                | 36.7 ms: 1.04x slower                                          |
| 2to3                       | 267 ms                                                 | 278 ms: 1.04x slower                                           |
| regex_compile              | 132 ms                                                 | 138 ms: 1.05x slower                                           |
| regex_dna                  | 218 ms                                                 | 229 ms: 1.05x slower                                           |
| sqlglot_transpile          | 1.58 ms                                                | 1.68 ms: 1.06x slower                                          |
| async_generators           | 436 ms                                                 | 463 ms: 1.06x slower                                           |
| genshi_text                | 23.5 ms                                                | 25.0 ms: 1.06x slower                                          |
| sqlglot_normalize          | 108 ms                                                 | 115 ms: 1.06x slower                                           |
| async_tree_io              | 842 ms                                                 | 897 ms: 1.07x slower                                           |
| create_gc_cycles           | 2.41 ms                                                | 2.60 ms: 1.08x slower                                          |
| sympy_expand               | 463 ms                                                 | 502 ms: 1.08x slower                                           |
| bench_thread_pool          | 822 us                                                 | 897 us: 1.09x slower                                           |
| sympy_str                  | 275 ms                                                 | 301 ms: 1.10x slower                                           |
| sqlglot_optimize           | 53.7 ms                                                | 59.7 ms: 1.11x slower                                          |
| sphinx                     | 1.03 sec                                               | 1.16 sec: 1.12x slower                                         |
| hexiom                     | 6.16 ms                                                | 6.99 ms: 1.13x slower                                          |
| nqueens                    | 78.4 ms                                                | 89.3 ms: 1.14x slower                                          |
| docutils                   | 2.59 sec                                               | 2.96 sec: 1.14x slower                                         |
| sympy_sum                  | 150 ms                                                 | 176 ms: 1.17x slower                                           |
| genshi_xml                 | 50.9 ms                                                | 59.7 ms: 1.17x slower                                          |
| sympy_integrate            | 19.9 ms                                                | 23.4 ms: 1.18x slower                                          |
| pylint                     | 313 ms                                                 | 374 ms: 1.20x slower                                           |
| generators                 | 29.0 ms                                                | 35.4 ms: 1.22x slower                                          |
| bench_mp_pool              | 24.0 ms                                                | 84.4 ms: 3.52x slower                                          |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                   |

Benchmark hidden because not significant (6): async_tree_memoization, coroutines, unpickle_pure_python, deltablue, html5lib, scimark_sor
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241017-3.14.0a0-c2fad93-JIT/bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.012x faster
# HPT report

- Reliability score: 56.70% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x