# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.026x faster
- HPT reliability: 85.27%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 278 ms: 1.04x slower                                           |
| docutils       | 2.59 sec                                               | 2.94 sec: 1.13x slower                                         |
| html5lib       | 64.2 ms                                                | 65.0 ms: 1.01x slower                                          |
| tornado_http   | 92.4 ms                                                | 95.6 ms: 1.03x slower                                          |
| Geometric mean | (ref)                                                  | 1.05x slower                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 386 ms: 1.20x faster                                           |
| async_tree_none            | 351 ms                                                 | 319 ms: 1.10x faster                                           |
| async_tree_memoization     | 442 ms                                                 | 406 ms: 1.09x faster                                           |
| async_tree_none_tg         | 321 ms                                                 | 309 ms: 1.04x faster                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 551 ms: 1.01x slower                                           |
| asyncio_websockets         | 552 ms                                                 | 557 ms: 1.01x slower                                           |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.02x slower                                          |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                           |
| async_tree_io              | 842 ms                                                 | 886 ms: 1.05x slower                                           |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                   |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 79.2 ms                                                | 71.9 ms: 1.10x faster                                          |
| nbody          | 87.0 ms                                                | 80.1 ms: 1.09x faster                                          |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                  | 1.06x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.68 ms: 1.02x faster                                          |
| regex_v8       | 26.2 ms                                                | 26.4 ms: 1.01x slower                                          |
| regex_dna      | 218 ms                                                 | 227 ms: 1.04x slower                                           |
| regex_compile  | 132 ms                                                 | 143 ms: 1.08x slower                                           |
| Geometric mean | (ref)                                                  | 1.03x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 77.6 ms: 1.12x faster                                          |
| xml_etree_process    | 60.6 ms                                                | 54.7 ms: 1.11x faster                                          |
| tomli_loads          | 2.14 sec                                               | 1.93 sec: 1.11x faster                                         |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.07x faster                                           |
| json_dumps           | 10.6 ms                                                | 10.2 ms: 1.03x faster                                          |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                          |
| pickle_pure_python   | 310 us                                                 | 302 us: 1.03x faster                                           |
| json_loads           | 27.2 us                                                | 27.0 us: 1.01x faster                                          |
| unpickle_pure_python | 216 us                                                 | 216 us: 1.00x slower                                           |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                          |
| python_startup_no_site | 6.96 ms                                                | 7.10 ms: 1.02x slower                                          |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.94 ms: 1.11x faster                                          |
| django_template | 35.2 ms                                                | 35.8 ms: 1.02x slower                                          |
| genshi_text     | 23.5 ms                                                | 25.4 ms: 1.08x slower                                          |
| genshi_xml      | 50.9 ms                                                | 58.2 ms: 1.14x slower                                          |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 27.1 us: 1.44x faster                                          |
| create_gc_cycles           | 2.41 ms                                                | 1.73 ms: 1.39x faster                                          |
| deepcopy                   | 358 us                                                 | 263 us: 1.36x faster                                           |
| deepcopy_reduce            | 3.20 us                                                | 2.66 us: 1.21x faster                                          |
| async_tree_memoization_tg  | 464 ms                                                 | 386 ms: 1.20x faster                                           |
| richards_super             | 54.9 ms                                                | 45.8 ms: 1.20x faster                                          |
| scimark_fft                | 364 ms                                                 | 305 ms: 1.19x faster                                           |
| richards                   | 48.7 ms                                                | 41.0 ms: 1.19x faster                                          |
| python_startup             | 12.5 ms                                                | 10.6 ms: 1.18x faster                                          |
| gc_traversal               | 4.37 ms                                                | 3.75 ms: 1.17x faster                                          |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.37 ms: 1.15x faster                                          |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                           |
| telco                      | 8.54 ms                                                | 7.62 ms: 1.12x faster                                          |
| xml_etree_generate         | 86.7 ms                                                | 77.6 ms: 1.12x faster                                          |
| crypto_pyaes               | 75.3 ms                                                | 67.4 ms: 1.12x faster                                          |
| mako                       | 11.1 ms                                                | 9.94 ms: 1.11x faster                                          |
| xml_etree_process          | 60.6 ms                                                | 54.7 ms: 1.11x faster                                          |
| tomli_loads                | 2.14 sec                                               | 1.93 sec: 1.11x faster                                         |
| pathlib                    | 17.5 ms                                                | 15.9 ms: 1.11x faster                                          |
| float                      | 79.2 ms                                                | 71.9 ms: 1.10x faster                                          |
| async_tree_none            | 351 ms                                                 | 319 ms: 1.10x faster                                           |
| async_tree_memoization     | 442 ms                                                 | 406 ms: 1.09x faster                                           |
| nbody                      | 87.0 ms                                                | 80.1 ms: 1.09x faster                                          |
| fannkuch                   | 404 ms                                                 | 374 ms: 1.08x faster                                           |
| json                       | 5.36 ms                                                | 4.96 ms: 1.08x faster                                          |
| go                         | 144 ms                                                 | 134 ms: 1.07x faster                                           |
| xml_etree_parse            | 156 ms                                                 | 145 ms: 1.07x faster                                           |
| bpe_tokeniser              | 4.75 sec                                               | 4.47 sec: 1.06x faster                                         |
| scimark_monte_carlo        | 67.4 ms                                                | 64.0 ms: 1.05x faster                                          |
| pprint_safe_repr           | 728 ms                                                 | 698 ms: 1.04x faster                                           |
| scimark_sor                | 124 ms                                                 | 118 ms: 1.04x faster                                           |
| async_tree_none_tg         | 321 ms                                                 | 309 ms: 1.04x faster                                           |
| json_dumps                 | 10.6 ms                                                | 10.2 ms: 1.03x faster                                          |
| logging_format             | 6.40 us                                                | 6.19 us: 1.03x faster                                          |
| pprint_pformat             | 1.49 sec                                               | 1.45 sec: 1.03x faster                                         |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                          |
| pyflate                    | 471 ms                                                 | 457 ms: 1.03x faster                                           |
| scimark_lu                 | 113 ms                                                 | 110 ms: 1.03x faster                                           |
| pickle_pure_python         | 310 us                                                 | 302 us: 1.03x faster                                           |
| thrift                     | 809 us                                                 | 790 us: 1.02x faster                                           |
| logging_silent             | 102 ns                                                 | 100.0 ns: 1.02x faster                                         |
| regex_effbot               | 3.73 ms                                                | 3.68 ms: 1.02x faster                                          |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                           |
| typing_runtime_protocols   | 165 us                                                 | 163 us: 1.01x faster                                           |
| logging_simple             | 5.72 us                                                | 5.67 us: 1.01x faster                                          |
| json_loads                 | 27.2 us                                                | 27.0 us: 1.01x faster                                          |
| pidigits                   | 186 ms                                                 | 185 ms: 1.01x faster                                           |
| deltablue                  | 3.23 ms                                                | 3.21 ms: 1.00x faster                                          |
| mdp                        | 2.72 sec                                               | 2.71 sec: 1.00x faster                                         |
| unpickle_pure_python       | 216 us                                                 | 216 us: 1.00x slower                                           |
| regex_v8                   | 26.2 ms                                                | 26.4 ms: 1.01x slower                                          |
| pycparser                  | 1.20 sec                                               | 1.21 sec: 1.01x slower                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 551 ms: 1.01x slower                                           |
| asyncio_websockets         | 552 ms                                                 | 557 ms: 1.01x slower                                           |
| html5lib                   | 64.2 ms                                                | 65.0 ms: 1.01x slower                                          |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.02x slower                                          |
| django_template            | 35.2 ms                                                | 35.8 ms: 1.02x slower                                          |
| python_startup_no_site     | 6.96 ms                                                | 7.10 ms: 1.02x slower                                          |
| coverage                   | 84.0 ms                                                | 85.8 ms: 1.02x slower                                          |
| raytrace                   | 267 ms                                                 | 276 ms: 1.03x slower                                           |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                          |
| tornado_http               | 92.4 ms                                                | 95.6 ms: 1.03x slower                                          |
| regex_dna                  | 218 ms                                                 | 227 ms: 1.04x slower                                           |
| 2to3                       | 267 ms                                                 | 278 ms: 1.04x slower                                           |
| chaos                      | 58.1 ms                                                | 60.7 ms: 1.04x slower                                          |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                           |
| async_tree_io              | 842 ms                                                 | 886 ms: 1.05x slower                                           |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.05x slower                                          |
| dulwich_log                | 64.3 ms                                                | 68.5 ms: 1.07x slower                                          |
| sqlglot_transpile          | 1.58 ms                                                | 1.69 ms: 1.07x slower                                          |
| sqlglot_normalize          | 108 ms                                                 | 115 ms: 1.07x slower                                           |
| sympy_expand               | 463 ms                                                 | 499 ms: 1.08x slower                                           |
| regex_compile              | 132 ms                                                 | 143 ms: 1.08x slower                                           |
| genshi_text                | 23.5 ms                                                | 25.4 ms: 1.08x slower                                          |
| bench_thread_pool          | 822 us                                                 | 897 us: 1.09x slower                                           |
| sympy_str                  | 275 ms                                                 | 300 ms: 1.09x slower                                           |
| nqueens                    | 78.4 ms                                                | 85.8 ms: 1.09x slower                                          |
| sqlglot_optimize           | 53.7 ms                                                | 59.9 ms: 1.11x slower                                          |
| docutils                   | 2.59 sec                                               | 2.94 sec: 1.13x slower                                         |
| hexiom                     | 6.16 ms                                                | 6.99 ms: 1.13x slower                                          |
| genshi_xml                 | 50.9 ms                                                | 58.2 ms: 1.14x slower                                          |
| sympy_sum                  | 150 ms                                                 | 177 ms: 1.18x slower                                           |
| sympy_integrate            | 19.9 ms                                                | 23.4 ms: 1.18x slower                                          |
| pylint                     | 313 ms                                                 | 373 ms: 1.19x slower                                           |
| generators                 | 29.0 ms                                                | 35.1 ms: 1.21x slower                                          |
| bench_mp_pool              | 24.0 ms                                                | 61.3 ms: 2.56x slower                                          |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_io_tg
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241007-3.14.0a0-aa18ec3-JIT/bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.026x faster
# HPT report

- Reliability score: 85.27% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x