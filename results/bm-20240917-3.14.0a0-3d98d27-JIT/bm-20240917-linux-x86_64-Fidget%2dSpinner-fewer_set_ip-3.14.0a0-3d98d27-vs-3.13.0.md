# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: fewer_set_ip
- machine: linux-x86_64
- commit hash: 3d98d27
- commit date: 2024-09-17
- overall geometric mean: 1.035x faster
- HPT reliability: 87.41%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 275 ms: 1.03x slower                                                    |
| docutils       | 2.59 sec                                               | 2.96 sec: 1.14x slower                                                  |
| html5lib       | 64.2 ms                                                | 65.6 ms: 1.02x slower                                                   |
| tornado_http   | 92.4 ms                                                | 94.8 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 388 ms: 1.20x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 398 ms: 1.11x faster                                                    |
| async_tree_none            | 351 ms                                                 | 317 ms: 1.11x faster                                                    |
| async_tree_none_tg         | 321 ms                                                 | 308 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 566 ms: 1.02x faster                                                    |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.00x slower                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 552 ms: 1.01x slower                                                    |
| async_tree_io_tg           | 857 ms                                                 | 877 ms: 1.02x slower                                                    |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                   |
| async_tree_io              | 842 ms                                                 | 863 ms: 1.03x slower                                                    |
| async_generators           | 436 ms                                                 | 453 ms: 1.04x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 69.1 ms: 1.15x faster                                                   |
| nbody          | 87.0 ms                                                | 82.1 ms: 1.06x faster                                                   |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.07x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.5 ms: 1.07x faster                                                   |
| regex_dna      | 218 ms                                                 | 228 ms: 1.04x slower                                                    |
| regex_compile  | 132 ms                                                 | 141 ms: 1.06x slower                                                    |
| regex_effbot   | 3.73 ms                                                | 4.01 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.90 sec: 1.13x faster                                                  |
| xml_etree_process    | 60.6 ms                                                | 53.9 ms: 1.13x faster                                                   |
| xml_etree_generate   | 86.7 ms                                                | 77.5 ms: 1.12x faster                                                   |
| xml_etree_parse      | 156 ms                                                 | 144 ms: 1.08x faster                                                    |
| xml_etree_iterparse  | 101 ms                                                 | 97.8 ms: 1.04x faster                                                   |
| json_dumps           | 10.6 ms                                                | 10.3 ms: 1.03x faster                                                   |
| pickle_pure_python   | 310 us                                                 | 307 us: 1.01x faster                                                    |
| json_loads           | 27.2 us                                                | 27.0 us: 1.01x faster                                                   |
| unpickle_pure_python | 216 us                                                 | 214 us: 1.01x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                   |
| python_startup_no_site | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 11.1 ms                                                | 9.80 ms: 1.13x faster                                                   |
| genshi_text    | 23.5 ms                                                | 24.3 ms: 1.03x slower                                                   |
| genshi_xml     | 50.9 ms                                                | 57.3 ms: 1.13x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 26.7 us: 1.46x faster                                                   |
| create_gc_cycles           | 2.41 ms                                                | 1.75 ms: 1.38x faster                                                   |
| deepcopy                   | 358 us                                                 | 267 us: 1.34x faster                                                    |
| richards                   | 48.7 ms                                                | 39.5 ms: 1.23x faster                                                   |
| richards_super             | 54.9 ms                                                | 45.0 ms: 1.22x faster                                                   |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.14 ms: 1.22x faster                                                   |
| deepcopy_reduce            | 3.20 us                                                | 2.63 us: 1.22x faster                                                   |
| scimark_fft                | 364 ms                                                 | 301 ms: 1.21x faster                                                    |
| async_tree_memoization_tg  | 464 ms                                                 | 388 ms: 1.20x faster                                                    |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                   |
| gc_traversal               | 4.37 ms                                                | 3.74 ms: 1.17x faster                                                   |
| crypto_pyaes               | 75.3 ms                                                | 65.4 ms: 1.15x faster                                                   |
| float                      | 79.2 ms                                                | 69.1 ms: 1.15x faster                                                   |
| mako                       | 11.1 ms                                                | 9.80 ms: 1.13x faster                                                   |
| tomli_loads                | 2.14 sec                                               | 1.90 sec: 1.13x faster                                                  |
| xml_etree_process          | 60.6 ms                                                | 53.9 ms: 1.13x faster                                                   |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                    |
| xml_etree_generate         | 86.7 ms                                                | 77.5 ms: 1.12x faster                                                   |
| async_tree_memoization     | 442 ms                                                 | 398 ms: 1.11x faster                                                    |
| async_tree_none            | 351 ms                                                 | 317 ms: 1.11x faster                                                    |
| pathlib                    | 17.5 ms                                                | 15.9 ms: 1.10x faster                                                   |
| go                         | 144 ms                                                 | 131 ms: 1.10x faster                                                    |
| fannkuch                   | 404 ms                                                 | 369 ms: 1.09x faster                                                    |
| scimark_monte_carlo        | 67.4 ms                                                | 61.9 ms: 1.09x faster                                                   |
| telco                      | 8.54 ms                                                | 7.91 ms: 1.08x faster                                                   |
| xml_etree_parse            | 156 ms                                                 | 144 ms: 1.08x faster                                                    |
| regex_v8                   | 26.2 ms                                                | 24.5 ms: 1.07x faster                                                   |
| bpe_tokeniser              | 4.75 sec                                               | 4.43 sec: 1.07x faster                                                  |
| mdp                        | 2.72 sec                                               | 2.56 sec: 1.06x faster                                                  |
| nbody                      | 87.0 ms                                                | 82.1 ms: 1.06x faster                                                   |
| logging_format             | 6.40 us                                                | 6.05 us: 1.06x faster                                                   |
| scimark_sor                | 124 ms                                                 | 117 ms: 1.06x faster                                                    |
| pyflate                    | 471 ms                                                 | 448 ms: 1.05x faster                                                    |
| json                       | 5.36 ms                                                | 5.12 ms: 1.05x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.05x faster                                                  |
| async_tree_none_tg         | 321 ms                                                 | 308 ms: 1.04x faster                                                    |
| scimark_lu                 | 113 ms                                                 | 109 ms: 1.04x faster                                                    |
| logging_simple             | 5.72 us                                                | 5.52 us: 1.04x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 97.8 ms: 1.04x faster                                                   |
| thrift                     | 809 us                                                 | 783 us: 1.03x faster                                                    |
| meteor_contest             | 109 ms                                                 | 105 ms: 1.03x faster                                                    |
| json_dumps                 | 10.6 ms                                                | 10.3 ms: 1.03x faster                                                   |
| typing_runtime_protocols   | 165 us                                                 | 160 us: 1.03x faster                                                    |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 566 ms: 1.02x faster                                                    |
| pickle_pure_python         | 310 us                                                 | 307 us: 1.01x faster                                                    |
| json_loads                 | 27.2 us                                                | 27.0 us: 1.01x faster                                                   |
| unpickle_pure_python       | 216 us                                                 | 214 us: 1.01x faster                                                    |
| deltablue                  | 3.23 ms                                                | 3.21 ms: 1.01x faster                                                   |
| pidigits                   | 186 ms                                                 | 185 ms: 1.01x faster                                                    |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.00x slower                                                    |
| chaos                      | 58.1 ms                                                | 58.6 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 552 ms: 1.01x slower                                                    |
| python_startup_no_site     | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                   |
| coverage                   | 84.0 ms                                                | 85.0 ms: 1.01x slower                                                   |
| bench_thread_pool          | 822 us                                                 | 836 us: 1.02x slower                                                    |
| pprint_safe_repr           | 728 ms                                                 | 743 ms: 1.02x slower                                                    |
| html5lib                   | 64.2 ms                                                | 65.6 ms: 1.02x slower                                                   |
| async_tree_io_tg           | 857 ms                                                 | 877 ms: 1.02x slower                                                    |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                   |
| async_tree_io              | 842 ms                                                 | 863 ms: 1.03x slower                                                    |
| tornado_http               | 92.4 ms                                                | 94.8 ms: 1.03x slower                                                   |
| 2to3                       | 267 ms                                                 | 275 ms: 1.03x slower                                                    |
| genshi_text                | 23.5 ms                                                | 24.3 ms: 1.03x slower                                                   |
| raytrace                   | 267 ms                                                 | 277 ms: 1.04x slower                                                    |
| async_generators           | 436 ms                                                 | 453 ms: 1.04x slower                                                    |
| regex_dna                  | 218 ms                                                 | 228 ms: 1.04x slower                                                    |
| pprint_pformat             | 1.49 sec                                               | 1.57 sec: 1.05x slower                                                  |
| sqlglot_normalize          | 108 ms                                                 | 113 ms: 1.05x slower                                                    |
| dulwich_log                | 64.3 ms                                                | 67.8 ms: 1.05x slower                                                   |
| sqlglot_parse              | 1.27 ms                                                | 1.35 ms: 1.06x slower                                                   |
| regex_compile              | 132 ms                                                 | 141 ms: 1.06x slower                                                    |
| sqlglot_transpile          | 1.58 ms                                                | 1.69 ms: 1.07x slower                                                   |
| sympy_str                  | 275 ms                                                 | 295 ms: 1.07x slower                                                    |
| regex_effbot               | 3.73 ms                                                | 4.01 ms: 1.07x slower                                                   |
| sympy_expand               | 463 ms                                                 | 499 ms: 1.08x slower                                                    |
| sqlglot_optimize           | 53.7 ms                                                | 57.9 ms: 1.08x slower                                                   |
| nqueens                    | 78.4 ms                                                | 85.0 ms: 1.09x slower                                                   |
| hexiom                     | 6.16 ms                                                | 6.84 ms: 1.11x slower                                                   |
| genshi_xml                 | 50.9 ms                                                | 57.3 ms: 1.13x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 170 ms: 1.13x slower                                                    |
| sympy_integrate            | 19.9 ms                                                | 22.6 ms: 1.14x slower                                                   |
| docutils                   | 2.59 sec                                               | 2.96 sec: 1.14x slower                                                  |
| generators                 | 29.0 ms                                                | 33.3 ms: 1.15x slower                                                   |
| pylint                     | 313 ms                                                 | 371 ms: 1.19x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                            |

Benchmark hidden because not significant (4): logging_silent, comprehensions, bench_mp_pool, django_template
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240917-3.14.0a0-3d98d27-JIT/bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.035x faster
# HPT report

- Reliability score: 87.41% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x