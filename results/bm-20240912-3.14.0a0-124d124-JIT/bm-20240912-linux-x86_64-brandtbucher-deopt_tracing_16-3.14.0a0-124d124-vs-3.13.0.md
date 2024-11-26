# Results vs. 3.13.0

- fork: brandtbucher
- ref: deopt_tracing_16
- machine: linux-x86_64
- commit hash: 124d124
- commit date: 2024-09-12
- overall geometric mean: 1.021x faster
- HPT reliability: 75.81%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 283 ms: 1.06x slower                                                    |
| docutils       | 2.59 sec                                               | 2.97 sec: 1.15x slower                                                  |
| html5lib       | 64.2 ms                                                | 65.1 ms: 1.01x slower                                                   |
| tornado_http   | 92.4 ms                                                | 94.7 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 388 ms: 1.19x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 396 ms: 1.12x faster                                                    |
| async_tree_none            | 351 ms                                                 | 314 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 321 ms                                                 | 308 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 566 ms: 1.02x faster                                                    |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 552 ms: 1.01x slower                                                    |
| async_generators           | 436 ms                                                 | 455 ms: 1.05x slower                                                    |
| async_tree_io              | 842 ms                                                 | 885 ms: 1.05x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                            |

Benchmark hidden because not significant (2): coroutines, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 69.4 ms: 1.14x faster                                                   |
| nbody          | 87.0 ms                                                | 81.1 ms: 1.07x faster                                                   |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                  | 1.07x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.0 ms: 1.09x faster                                                   |
| regex_dna      | 218 ms                                                 | 221 ms: 1.01x slower                                                    |
| regex_effbot   | 3.73 ms                                                | 3.78 ms: 1.01x slower                                                   |
| regex_compile  | 132 ms                                                 | 144 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 77.6 ms: 1.12x faster                                                   |
| xml_etree_process    | 60.6 ms                                                | 54.5 ms: 1.11x faster                                                   |
| tomli_loads          | 2.14 sec                                               | 1.94 sec: 1.10x faster                                                  |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.08x faster                                                    |
| json_dumps           | 10.6 ms                                                | 10.1 ms: 1.05x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 98.7 ms: 1.03x faster                                                   |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.00x slower                                                    |
| json_loads           | 27.2 us                                                | 27.4 us: 1.01x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                            |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                   |
| python_startup_no_site | 6.96 ms                                                | 7.02 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.71 ms: 1.14x faster                                                   |
| django_template | 35.2 ms                                                | 37.4 ms: 1.07x slower                                                   |
| genshi_text     | 23.5 ms                                                | 25.7 ms: 1.09x slower                                                   |
| genshi_xml      | 50.9 ms                                                | 59.8 ms: 1.17x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 27.1 us: 1.44x faster                                                   |
| create_gc_cycles           | 2.41 ms                                                | 1.76 ms: 1.37x faster                                                   |
| deepcopy                   | 358 us                                                 | 268 us: 1.34x faster                                                    |
| gc_traversal               | 4.37 ms                                                | 3.53 ms: 1.24x faster                                                   |
| deepcopy_reduce            | 3.20 us                                                | 2.65 us: 1.21x faster                                                   |
| async_tree_memoization_tg  | 464 ms                                                 | 388 ms: 1.19x faster                                                    |
| scimark_fft                | 364 ms                                                 | 306 ms: 1.19x faster                                                    |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                   |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.33 ms: 1.16x faster                                                   |
| crypto_pyaes               | 75.3 ms                                                | 65.9 ms: 1.14x faster                                                   |
| float                      | 79.2 ms                                                | 69.4 ms: 1.14x faster                                                   |
| mako                       | 11.1 ms                                                | 9.71 ms: 1.14x faster                                                   |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                    |
| xml_etree_generate         | 86.7 ms                                                | 77.6 ms: 1.12x faster                                                   |
| async_tree_memoization     | 442 ms                                                 | 396 ms: 1.12x faster                                                    |
| async_tree_none            | 351 ms                                                 | 314 ms: 1.12x faster                                                    |
| xml_etree_process          | 60.6 ms                                                | 54.5 ms: 1.11x faster                                                   |
| tomli_loads                | 2.14 sec                                               | 1.94 sec: 1.10x faster                                                  |
| pathlib                    | 17.5 ms                                                | 16.0 ms: 1.10x faster                                                   |
| regex_v8                   | 26.2 ms                                                | 24.0 ms: 1.09x faster                                                   |
| telco                      | 8.54 ms                                                | 7.86 ms: 1.09x faster                                                   |
| fannkuch                   | 404 ms                                                 | 375 ms: 1.08x faster                                                    |
| pyflate                    | 471 ms                                                 | 437 ms: 1.08x faster                                                    |
| xml_etree_parse            | 156 ms                                                 | 145 ms: 1.08x faster                                                    |
| richards_super             | 54.9 ms                                                | 51.1 ms: 1.07x faster                                                   |
| mdp                        | 2.72 sec                                               | 2.54 sec: 1.07x faster                                                  |
| nbody                      | 87.0 ms                                                | 81.1 ms: 1.07x faster                                                   |
| bpe_tokeniser              | 4.75 sec                                               | 4.43 sec: 1.07x faster                                                  |
| scimark_monte_carlo        | 67.4 ms                                                | 63.0 ms: 1.07x faster                                                   |
| scimark_sor                | 124 ms                                                 | 117 ms: 1.06x faster                                                    |
| logging_format             | 6.40 us                                                | 6.05 us: 1.06x faster                                                   |
| go                         | 144 ms                                                 | 137 ms: 1.05x faster                                                    |
| json_dumps                 | 10.6 ms                                                | 10.1 ms: 1.05x faster                                                   |
| richards                   | 48.7 ms                                                | 46.7 ms: 1.04x faster                                                   |
| json                       | 5.36 ms                                                | 5.14 ms: 1.04x faster                                                   |
| async_tree_none_tg         | 321 ms                                                 | 308 ms: 1.04x faster                                                    |
| scimark_lu                 | 113 ms                                                 | 109 ms: 1.04x faster                                                    |
| logging_simple             | 5.72 us                                                | 5.52 us: 1.04x faster                                                   |
| meteor_contest             | 109 ms                                                 | 105 ms: 1.03x faster                                                    |
| xml_etree_iterparse        | 101 ms                                                 | 98.7 ms: 1.03x faster                                                   |
| thrift                     | 809 us                                                 | 791 us: 1.02x faster                                                    |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 566 ms: 1.02x faster                                                    |
| pycparser                  | 1.20 sec                                               | 1.19 sec: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| unpickle_pure_python       | 216 us                                                 | 217 us: 1.00x slower                                                    |
| json_loads                 | 27.2 us                                                | 27.4 us: 1.01x slower                                                   |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                    |
| logging_silent             | 102 ns                                                 | 102 ns: 1.01x slower                                                    |
| coverage                   | 84.0 ms                                                | 84.6 ms: 1.01x slower                                                   |
| python_startup_no_site     | 6.96 ms                                                | 7.02 ms: 1.01x slower                                                   |
| regex_dna                  | 218 ms                                                 | 221 ms: 1.01x slower                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 552 ms: 1.01x slower                                                    |
| regex_effbot               | 3.73 ms                                                | 3.78 ms: 1.01x slower                                                   |
| html5lib                   | 64.2 ms                                                | 65.1 ms: 1.01x slower                                                   |
| bench_thread_pool          | 822 us                                                 | 833 us: 1.01x slower                                                    |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.02x slower                                                   |
| pprint_safe_repr           | 728 ms                                                 | 745 ms: 1.02x slower                                                    |
| tornado_http               | 92.4 ms                                                | 94.7 ms: 1.02x slower                                                   |
| pprint_pformat             | 1.49 sec                                               | 1.55 sec: 1.04x slower                                                  |
| async_generators           | 436 ms                                                 | 455 ms: 1.05x slower                                                    |
| async_tree_io              | 842 ms                                                 | 885 ms: 1.05x slower                                                    |
| dulwich_log                | 64.3 ms                                                | 68.0 ms: 1.06x slower                                                   |
| 2to3                       | 267 ms                                                 | 283 ms: 1.06x slower                                                    |
| django_template            | 35.2 ms                                                | 37.4 ms: 1.07x slower                                                   |
| raytrace                   | 267 ms                                                 | 286 ms: 1.07x slower                                                    |
| sqlglot_parse              | 1.27 ms                                                | 1.37 ms: 1.07x slower                                                   |
| sqlglot_transpile          | 1.58 ms                                                | 1.71 ms: 1.08x slower                                                   |
| regex_compile              | 132 ms                                                 | 144 ms: 1.09x slower                                                    |
| genshi_text                | 23.5 ms                                                | 25.7 ms: 1.09x slower                                                   |
| sqlglot_optimize           | 53.7 ms                                                | 59.1 ms: 1.10x slower                                                   |
| nqueens                    | 78.4 ms                                                | 86.5 ms: 1.10x slower                                                   |
| sympy_str                  | 275 ms                                                 | 307 ms: 1.12x slower                                                    |
| sympy_expand               | 463 ms                                                 | 521 ms: 1.12x slower                                                    |
| sqlglot_normalize          | 108 ms                                                 | 122 ms: 1.13x slower                                                    |
| hexiom                     | 6.16 ms                                                | 7.00 ms: 1.14x slower                                                   |
| deltablue                  | 3.23 ms                                                | 3.66 ms: 1.14x slower                                                   |
| docutils                   | 2.59 sec                                               | 2.97 sec: 1.15x slower                                                  |
| generators                 | 29.0 ms                                                | 33.6 ms: 1.16x slower                                                   |
| genshi_xml                 | 50.9 ms                                                | 59.8 ms: 1.17x slower                                                   |
| sympy_integrate            | 19.9 ms                                                | 23.4 ms: 1.18x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 177 ms: 1.18x slower                                                    |
| pylint                     | 313 ms                                                 | 385 ms: 1.23x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (6): typing_runtime_protocols, coroutines, bench_mp_pool, chaos, pickle_pure_python, async_tree_io_tg
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240912-3.14.0a0-124d124-JIT/bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.021x faster
# HPT report

- Reliability score: 75.81% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x