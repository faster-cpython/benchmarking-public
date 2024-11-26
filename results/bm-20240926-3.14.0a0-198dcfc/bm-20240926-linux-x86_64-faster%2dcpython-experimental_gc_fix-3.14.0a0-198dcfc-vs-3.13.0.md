# Results vs. 3.13.0

- fork: faster-cpython
- ref: experimental_gc_fix
- machine: linux-x86_64
- commit hash: 198dcfc
- commit date: 2024-09-26
- overall geometric mean: 1.003x faster
- HPT reliability: 63.60%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 271 ms: 1.02x slower                                                           |
| docutils       | 2.59 sec                                               | 2.70 sec: 1.04x slower                                                         |
| html5lib       | 64.2 ms                                                | 68.1 ms: 1.06x slower                                                          |
| tornado_http   | 92.4 ms                                                | 91.8 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                           |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.02x slower                                                          |
| async_generators           | 436 ms                                                 | 455 ms: 1.05x slower                                                           |
| async_tree_memoization_tg  | 464 ms                                                 | 498 ms: 1.07x slower                                                           |
| async_tree_memoization     | 442 ms                                                 | 481 ms: 1.09x slower                                                           |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 644 ms: 1.12x slower                                                           |
| async_tree_io_tg           | 857 ms                                                 | 959 ms: 1.12x slower                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 627 ms: 1.15x slower                                                           |
| async_tree_io              | 842 ms                                                 | 987 ms: 1.17x slower                                                           |
| async_tree_none_tg         | 321 ms                                                 | 386 ms: 1.20x slower                                                           |
| async_tree_none            | 351 ms                                                 | 424 ms: 1.21x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.11x slower                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 86.4 ms: 1.01x faster                                                          |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                           |
| float          | 79.2 ms                                                | 95.9 ms: 1.21x slower                                                          |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.1 ms: 1.05x faster                                                          |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                           |
| regex_effbot   | 3.73 ms                                                | 3.64 ms: 1.03x faster                                                          |
| regex_dna      | 218 ms                                                 | 222 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 2.07 sec: 1.04x faster                                                         |
| pickle_pure_python   | 310 us                                                 | 303 us: 1.03x faster                                                           |
| unpickle_pure_python | 216 us                                                 | 211 us: 1.02x faster                                                           |
| json_dumps           | 10.6 ms                                                | 10.4 ms: 1.02x faster                                                          |
| xml_etree_generate   | 86.7 ms                                                | 91.0 ms: 1.05x slower                                                          |
| xml_etree_process    | 60.6 ms                                                | 65.2 ms: 1.07x slower                                                          |
| xml_etree_parse      | 156 ms                                                 | 171 ms: 1.10x slower                                                           |
| xml_etree_iterparse  | 101 ms                                                 | 157 ms: 1.55x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.06x slower                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.7 ms: 1.17x faster                                                          |
| python_startup_no_site | 6.96 ms                                                | 7.01 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.1 ms: 1.07x faster                                                          |
| django_template | 35.2 ms                                                | 34.2 ms: 1.03x faster                                                          |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                          |
| genshi_xml      | 50.9 ms                                                | 54.5 ms: 1.07x slower                                                          |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.71 ms: 1.41x faster                                                          |
| deepcopy                   | 358 us                                                 | 256 us: 1.40x faster                                                           |
| deepcopy_memo              | 39.1 us                                                | 29.6 us: 1.32x faster                                                          |
| gc_traversal               | 4.37 ms                                                | 3.53 ms: 1.24x faster                                                          |
| go                         | 144 ms                                                 | 117 ms: 1.23x faster                                                           |
| deepcopy_reduce            | 3.20 us                                                | 2.65 us: 1.21x faster                                                          |
| python_startup             | 12.5 ms                                                | 10.7 ms: 1.17x faster                                                          |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                          |
| mdp                        | 2.72 sec                                               | 2.53 sec: 1.08x faster                                                         |
| genshi_text                | 23.5 ms                                                | 22.1 ms: 1.07x faster                                                          |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.74 ms: 1.06x faster                                                          |
| richards                   | 48.7 ms                                                | 45.9 ms: 1.06x faster                                                          |
| richards_super             | 54.9 ms                                                | 51.9 ms: 1.06x faster                                                          |
| generators                 | 29.0 ms                                                | 27.6 ms: 1.05x faster                                                          |
| crypto_pyaes               | 75.3 ms                                                | 71.9 ms: 1.05x faster                                                          |
| regex_v8                   | 26.2 ms                                                | 25.1 ms: 1.05x faster                                                          |
| thrift                     | 809 us                                                 | 776 us: 1.04x faster                                                           |
| bench_thread_pool          | 822 us                                                 | 790 us: 1.04x faster                                                           |
| json                       | 5.36 ms                                                | 5.17 ms: 1.04x faster                                                          |
| tomli_loads                | 2.14 sec                                               | 2.07 sec: 1.04x faster                                                         |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.03x faster                                                           |
| typing_runtime_protocols   | 165 us                                                 | 160 us: 1.03x faster                                                           |
| logging_format             | 6.40 us                                                | 6.20 us: 1.03x faster                                                          |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                           |
| django_template            | 35.2 ms                                                | 34.2 ms: 1.03x faster                                                          |
| telco                      | 8.54 ms                                                | 8.30 ms: 1.03x faster                                                          |
| pprint_safe_repr           | 728 ms                                                 | 708 ms: 1.03x faster                                                           |
| pprint_pformat             | 1.49 sec                                               | 1.45 sec: 1.03x faster                                                         |
| sympy_str                  | 275 ms                                                 | 268 ms: 1.03x faster                                                           |
| regex_effbot               | 3.73 ms                                                | 3.64 ms: 1.03x faster                                                          |
| pickle_pure_python         | 310 us                                                 | 303 us: 1.03x faster                                                           |
| sympy_expand               | 463 ms                                                 | 453 ms: 1.02x faster                                                           |
| sympy_integrate            | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                          |
| raytrace                   | 267 ms                                                 | 261 ms: 1.02x faster                                                           |
| unpickle_pure_python       | 216 us                                                 | 211 us: 1.02x faster                                                           |
| json_dumps                 | 10.6 ms                                                | 10.4 ms: 1.02x faster                                                          |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                           |
| logging_simple             | 5.72 us                                                | 5.61 us: 1.02x faster                                                          |
| scimark_fft                | 364 ms                                                 | 358 ms: 1.02x faster                                                           |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.02x faster                                                           |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                           |
| scimark_monte_carlo        | 67.4 ms                                                | 66.8 ms: 1.01x faster                                                          |
| logging_silent             | 102 ns                                                 | 101 ns: 1.01x faster                                                           |
| nbody                      | 87.0 ms                                                | 86.4 ms: 1.01x faster                                                          |
| tornado_http               | 92.4 ms                                                | 91.8 ms: 1.01x faster                                                          |
| comprehensions             | 16.5 us                                                | 16.5 us: 1.00x slower                                                          |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                           |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                           |
| sqlglot_optimize           | 53.7 ms                                                | 54.1 ms: 1.01x slower                                                          |
| python_startup_no_site     | 6.96 ms                                                | 7.01 ms: 1.01x slower                                                          |
| chaos                      | 58.1 ms                                                | 58.5 ms: 1.01x slower                                                          |
| scimark_lu                 | 113 ms                                                 | 114 ms: 1.01x slower                                                           |
| pycparser                  | 1.20 sec                                               | 1.22 sec: 1.01x slower                                                         |
| mako                       | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                          |
| nqueens                    | 78.4 ms                                                | 79.5 ms: 1.01x slower                                                          |
| regex_dna                  | 218 ms                                                 | 222 ms: 1.01x slower                                                           |
| 2to3                       | 267 ms                                                 | 271 ms: 1.02x slower                                                           |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.02x slower                                                          |
| coverage                   | 84.0 ms                                                | 85.3 ms: 1.02x slower                                                          |
| deltablue                  | 3.23 ms                                                | 3.29 ms: 1.02x slower                                                          |
| sqlglot_transpile          | 1.58 ms                                                | 1.62 ms: 1.02x slower                                                          |
| sqlglot_parse              | 1.27 ms                                                | 1.31 ms: 1.03x slower                                                          |
| docutils                   | 2.59 sec                                               | 2.70 sec: 1.04x slower                                                         |
| async_generators           | 436 ms                                                 | 455 ms: 1.05x slower                                                           |
| xml_etree_generate         | 86.7 ms                                                | 91.0 ms: 1.05x slower                                                          |
| html5lib                   | 64.2 ms                                                | 68.1 ms: 1.06x slower                                                          |
| genshi_xml                 | 50.9 ms                                                | 54.5 ms: 1.07x slower                                                          |
| async_tree_memoization_tg  | 464 ms                                                 | 498 ms: 1.07x slower                                                           |
| xml_etree_process          | 60.6 ms                                                | 65.2 ms: 1.07x slower                                                          |
| async_tree_memoization     | 442 ms                                                 | 481 ms: 1.09x slower                                                           |
| xml_etree_parse            | 156 ms                                                 | 171 ms: 1.10x slower                                                           |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 644 ms: 1.12x slower                                                           |
| async_tree_io_tg           | 857 ms                                                 | 959 ms: 1.12x slower                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 627 ms: 1.15x slower                                                           |
| async_tree_io              | 842 ms                                                 | 987 ms: 1.17x slower                                                           |
| async_tree_none_tg         | 321 ms                                                 | 386 ms: 1.20x slower                                                           |
| float                      | 79.2 ms                                                | 95.9 ms: 1.21x slower                                                          |
| async_tree_none            | 351 ms                                                 | 424 ms: 1.21x slower                                                           |
| bpe_tokeniser              | 4.75 sec                                               | 5.76 sec: 1.21x slower                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 157 ms: 1.55x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                                   |

Benchmark hidden because not significant (8): scimark_sor, json_loads, fannkuch, bench_mp_pool, dulwich_log, hexiom, pyflate, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240926-3.14.0a0-198dcfc/bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.003x faster
# HPT report

- Reliability score: 63.60% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.90x