# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: f83c7c1
- commit date: 2024-10-04
- overall geometric mean: 1.003x faster
- HPT reliability: 57.60%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 291 ms: 1.09x slower                                             |
| docutils       | 2.59 sec                                               | 3.07 sec: 1.18x slower                                           |
| html5lib       | 64.2 ms                                                | 71.3 ms: 1.11x slower                                            |
| tornado_http   | 92.4 ms                                                | 102 ms: 1.11x slower                                             |
| Geometric mean | (ref)                                                  | 1.12x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 393 ms: 1.18x faster                                             |
| async_tree_none            | 351 ms                                                 | 324 ms: 1.08x faster                                             |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.07x faster                                             |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 569 ms: 1.01x faster                                             |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 557 ms: 1.02x slower                                             |
| async_tree_io_tg           | 857 ms                                                 | 877 ms: 1.02x slower                                             |
| coroutines                 | 22.7 ms                                                | 23.4 ms: 1.03x slower                                            |
| async_generators           | 436 ms                                                 | 454 ms: 1.04x slower                                             |
| async_tree_io              | 842 ms                                                 | 890 ms: 1.06x slower                                             |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                     |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 79.2 ms                                                | 71.3 ms: 1.11x faster                                            |
| nbody          | 87.0 ms                                                | 81.5 ms: 1.07x faster                                            |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                  | 1.06x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.7 ms: 1.06x faster                                            |
| regex_effbot   | 3.73 ms                                                | 3.67 ms: 1.02x faster                                            |
| regex_dna      | 218 ms                                                 | 217 ms: 1.01x faster                                             |
| regex_compile  | 132 ms                                                 | 155 ms: 1.17x slower                                             |
| Geometric mean | (ref)                                                  | 1.02x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 77.0 ms: 1.13x faster                                            |
| xml_etree_process    | 60.6 ms                                                | 55.4 ms: 1.09x faster                                            |
| unpickle_pure_python | 216 us                                                 | 202 us: 1.07x faster                                             |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                             |
| json_dumps           | 10.6 ms                                                | 10.1 ms: 1.05x faster                                            |
| xml_etree_iterparse  | 101 ms                                                 | 97.4 ms: 1.04x faster                                            |
| tomli_loads          | 2.14 sec                                               | 2.08 sec: 1.03x faster                                           |
| pickle_pure_python   | 310 us                                                 | 318 us: 1.02x slower                                             |
| json_loads           | 27.2 us                                                | 28.3 us: 1.04x slower                                            |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.18x faster                                            |
| python_startup_no_site | 6.96 ms                                                | 7.07 ms: 1.02x slower                                            |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.86 ms: 1.12x faster                                            |
| genshi_text     | 23.5 ms                                                | 24.3 ms: 1.03x slower                                            |
| django_template | 35.2 ms                                                | 41.1 ms: 1.17x slower                                            |
| genshi_xml      | 50.9 ms                                                | 70.3 ms: 1.38x slower                                            |
| Geometric mean  | (ref)                                                  | 1.10x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 26.6 us: 1.47x faster                                            |
| create_gc_cycles           | 2.41 ms                                                | 1.72 ms: 1.40x faster                                            |
| deepcopy                   | 358 us                                                 | 267 us: 1.34x faster                                             |
| richards                   | 48.7 ms                                                | 40.6 ms: 1.20x faster                                            |
| richards_super             | 54.9 ms                                                | 46.2 ms: 1.19x faster                                            |
| deepcopy_reduce            | 3.20 us                                                | 2.69 us: 1.19x faster                                            |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.18x faster                                            |
| gc_traversal               | 4.37 ms                                                | 3.69 ms: 1.18x faster                                            |
| async_tree_memoization_tg  | 464 ms                                                 | 393 ms: 1.18x faster                                             |
| scimark_fft                | 364 ms                                                 | 313 ms: 1.16x faster                                             |
| telco                      | 8.54 ms                                                | 7.51 ms: 1.14x faster                                            |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.44 ms: 1.14x faster                                            |
| xml_etree_generate         | 86.7 ms                                                | 77.0 ms: 1.13x faster                                            |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                             |
| scimark_monte_carlo        | 67.4 ms                                                | 60.0 ms: 1.13x faster                                            |
| crypto_pyaes               | 75.3 ms                                                | 67.0 ms: 1.12x faster                                            |
| mako                       | 11.1 ms                                                | 9.86 ms: 1.12x faster                                            |
| pathlib                    | 17.5 ms                                                | 15.7 ms: 1.12x faster                                            |
| float                      | 79.2 ms                                                | 71.3 ms: 1.11x faster                                            |
| xml_etree_process          | 60.6 ms                                                | 55.4 ms: 1.09x faster                                            |
| async_tree_none            | 351 ms                                                 | 324 ms: 1.08x faster                                             |
| mdp                        | 2.72 sec                                               | 2.52 sec: 1.08x faster                                           |
| bpe_tokeniser              | 4.75 sec                                               | 4.43 sec: 1.07x faster                                           |
| pyflate                    | 471 ms                                                 | 440 ms: 1.07x faster                                             |
| nbody                      | 87.0 ms                                                | 81.5 ms: 1.07x faster                                            |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.07x faster                                             |
| unpickle_pure_python       | 216 us                                                 | 202 us: 1.07x faster                                             |
| fannkuch                   | 404 ms                                                 | 380 ms: 1.06x faster                                             |
| json                       | 5.36 ms                                                | 5.05 ms: 1.06x faster                                            |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                             |
| regex_v8                   | 26.2 ms                                                | 24.7 ms: 1.06x faster                                            |
| go                         | 144 ms                                                 | 136 ms: 1.05x faster                                             |
| json_dumps                 | 10.6 ms                                                | 10.1 ms: 1.05x faster                                            |
| xml_etree_iterparse        | 101 ms                                                 | 97.4 ms: 1.04x faster                                            |
| thrift                     | 809 us                                                 | 784 us: 1.03x faster                                             |
| tomli_loads                | 2.14 sec                                               | 2.08 sec: 1.03x faster                                           |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.02x faster                                             |
| scimark_sor                | 124 ms                                                 | 122 ms: 1.02x faster                                             |
| regex_effbot               | 3.73 ms                                                | 3.67 ms: 1.02x faster                                            |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 569 ms: 1.01x faster                                             |
| regex_dna                  | 218 ms                                                 | 217 ms: 1.01x faster                                             |
| scimark_lu                 | 113 ms                                                 | 112 ms: 1.01x faster                                             |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                             |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                             |
| pprint_safe_repr           | 728 ms                                                 | 738 ms: 1.01x slower                                             |
| typing_runtime_protocols   | 165 us                                                 | 167 us: 1.01x slower                                             |
| python_startup_no_site     | 6.96 ms                                                | 7.07 ms: 1.02x slower                                            |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                            |
| deltablue                  | 3.23 ms                                                | 3.29 ms: 1.02x slower                                            |
| logging_format             | 6.40 us                                                | 6.52 us: 1.02x slower                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 557 ms: 1.02x slower                                             |
| async_tree_io_tg           | 857 ms                                                 | 877 ms: 1.02x slower                                             |
| pickle_pure_python         | 310 us                                                 | 318 us: 1.02x slower                                             |
| coverage                   | 84.0 ms                                                | 86.5 ms: 1.03x slower                                            |
| coroutines                 | 22.7 ms                                                | 23.4 ms: 1.03x slower                                            |
| genshi_text                | 23.5 ms                                                | 24.3 ms: 1.03x slower                                            |
| json_loads                 | 27.2 us                                                | 28.3 us: 1.04x slower                                            |
| chaos                      | 58.1 ms                                                | 60.4 ms: 1.04x slower                                            |
| async_generators           | 436 ms                                                 | 454 ms: 1.04x slower                                             |
| pprint_pformat             | 1.49 sec                                               | 1.56 sec: 1.05x slower                                           |
| logging_simple             | 5.72 us                                                | 5.99 us: 1.05x slower                                            |
| raytrace                   | 267 ms                                                 | 282 ms: 1.05x slower                                             |
| async_tree_io              | 842 ms                                                 | 890 ms: 1.06x slower                                             |
| pycparser                  | 1.20 sec                                               | 1.30 sec: 1.08x slower                                           |
| nqueens                    | 78.4 ms                                                | 85.1 ms: 1.09x slower                                            |
| 2to3                       | 267 ms                                                 | 291 ms: 1.09x slower                                             |
| logging_silent             | 102 ns                                                 | 111 ns: 1.09x slower                                             |
| bench_thread_pool          | 822 us                                                 | 902 us: 1.10x slower                                             |
| tornado_http               | 92.4 ms                                                | 102 ms: 1.11x slower                                             |
| html5lib                   | 64.2 ms                                                | 71.3 ms: 1.11x slower                                            |
| hexiom                     | 6.16 ms                                                | 6.97 ms: 1.13x slower                                            |
| dulwich_log                | 64.3 ms                                                | 73.6 ms: 1.14x slower                                            |
| sqlglot_transpile          | 1.58 ms                                                | 1.83 ms: 1.16x slower                                            |
| sympy_expand               | 463 ms                                                 | 537 ms: 1.16x slower                                             |
| sqlglot_normalize          | 108 ms                                                 | 126 ms: 1.17x slower                                             |
| django_template            | 35.2 ms                                                | 41.1 ms: 1.17x slower                                            |
| regex_compile              | 132 ms                                                 | 155 ms: 1.17x slower                                             |
| sympy_str                  | 275 ms                                                 | 323 ms: 1.18x slower                                             |
| docutils                   | 2.59 sec                                               | 3.07 sec: 1.18x slower                                           |
| sqlglot_optimize           | 53.7 ms                                                | 63.8 ms: 1.19x slower                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.54 ms: 1.21x slower                                            |
| generators                 | 29.0 ms                                                | 35.3 ms: 1.22x slower                                            |
| sympy_sum                  | 150 ms                                                 | 191 ms: 1.27x slower                                             |
| pylint                     | 313 ms                                                 | 400 ms: 1.28x slower                                             |
| sympy_integrate            | 19.9 ms                                                | 26.1 ms: 1.31x slower                                            |
| genshi_xml                 | 50.9 ms                                                | 70.3 ms: 1.38x slower                                            |
| bench_mp_pool              | 24.0 ms                                                | 60.9 ms: 2.54x slower                                            |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                     |

Benchmark hidden because not significant (1): async_tree_none_tg
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241004-3.14.0a0-f83c7c1-JIT/bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.003x faster
# HPT report

- Reliability score: 57.60% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x