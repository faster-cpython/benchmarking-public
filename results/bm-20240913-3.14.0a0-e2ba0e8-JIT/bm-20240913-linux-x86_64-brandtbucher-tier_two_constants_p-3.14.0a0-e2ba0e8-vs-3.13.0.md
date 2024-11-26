# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_constants_p
- machine: linux-x86_64
- commit hash: e2ba0e8
- commit date: 2024-09-13
- overall geometric mean: 1.027x faster
- HPT reliability: 80.28%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 280 ms: 1.05x slower                                                        |
| docutils       | 2.59 sec                                               | 2.97 sec: 1.14x slower                                                      |
| html5lib       | 64.2 ms                                                | 65.6 ms: 1.02x slower                                                       |
| tornado_http   | 92.4 ms                                                | 95.1 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 387 ms: 1.20x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 400 ms: 1.11x faster                                                        |
| async_tree_none            | 351 ms                                                 | 320 ms: 1.09x faster                                                        |
| async_tree_none_tg         | 321 ms                                                 | 307 ms: 1.04x faster                                                        |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                        |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 554 ms: 1.02x slower                                                        |
| async_tree_io              | 842 ms                                                 | 888 ms: 1.05x slower                                                        |
| async_generators           | 436 ms                                                 | 460 ms: 1.05x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 69.6 ms: 1.14x faster                                                       |
| nbody          | 87.0 ms                                                | 81.7 ms: 1.06x faster                                                       |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.59 ms: 1.04x faster                                                       |
| regex_v8       | 26.2 ms                                                | 25.4 ms: 1.03x faster                                                       |
| regex_dna      | 218 ms                                                 | 221 ms: 1.01x slower                                                        |
| regex_compile  | 132 ms                                                 | 142 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 76.9 ms: 1.13x faster                                                       |
| xml_etree_process    | 60.6 ms                                                | 54.1 ms: 1.12x faster                                                       |
| tomli_loads          | 2.14 sec                                               | 1.98 sec: 1.08x faster                                                      |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                        |
| json_dumps           | 10.6 ms                                                | 10.1 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 101 ms                                                 | 98.6 ms: 1.03x faster                                                       |
| pickle_pure_python   | 310 us                                                 | 303 us: 1.03x faster                                                        |
| json_loads           | 27.2 us                                                | 26.7 us: 1.02x faster                                                       |
| unpickle_pure_python | 216 us                                                 | 215 us: 1.00x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                       |
| python_startup_no_site | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.73 ms: 1.14x faster                                                       |
| django_template | 35.2 ms                                                | 35.8 ms: 1.02x slower                                                       |
| genshi_text     | 23.5 ms                                                | 25.8 ms: 1.10x slower                                                       |
| genshi_xml      | 50.9 ms                                                | 59.0 ms: 1.16x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 27.1 us: 1.44x faster                                                       |
| create_gc_cycles           | 2.41 ms                                                | 1.75 ms: 1.37x faster                                                       |
| deepcopy                   | 358 us                                                 | 277 us: 1.29x faster                                                        |
| richards                   | 48.7 ms                                                | 39.6 ms: 1.23x faster                                                       |
| richards_super             | 54.9 ms                                                | 45.1 ms: 1.22x faster                                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 387 ms: 1.20x faster                                                        |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                       |
| deepcopy_reduce            | 3.20 us                                                | 2.71 us: 1.18x faster                                                       |
| gc_traversal               | 4.37 ms                                                | 3.72 ms: 1.17x faster                                                       |
| spectral_norm              | 115 ms                                                 | 99.6 ms: 1.16x faster                                                       |
| scimark_fft                | 364 ms                                                 | 316 ms: 1.15x faster                                                        |
| mako                       | 11.1 ms                                                | 9.73 ms: 1.14x faster                                                       |
| float                      | 79.2 ms                                                | 69.6 ms: 1.14x faster                                                       |
| xml_etree_generate         | 86.7 ms                                                | 76.9 ms: 1.13x faster                                                       |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.47 ms: 1.13x faster                                                       |
| xml_etree_process          | 60.6 ms                                                | 54.1 ms: 1.12x faster                                                       |
| crypto_pyaes               | 75.3 ms                                                | 67.3 ms: 1.12x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 400 ms: 1.11x faster                                                        |
| async_tree_none            | 351 ms                                                 | 320 ms: 1.09x faster                                                        |
| go                         | 144 ms                                                 | 131 ms: 1.09x faster                                                        |
| pathlib                    | 17.5 ms                                                | 16.0 ms: 1.09x faster                                                       |
| tomli_loads                | 2.14 sec                                               | 1.98 sec: 1.08x faster                                                      |
| fannkuch                   | 404 ms                                                 | 374 ms: 1.08x faster                                                        |
| bpe_tokeniser              | 4.75 sec                                               | 4.40 sec: 1.08x faster                                                      |
| mdp                        | 2.72 sec                                               | 2.53 sec: 1.07x faster                                                      |
| json                       | 5.36 ms                                                | 5.02 ms: 1.07x faster                                                       |
| scimark_monte_carlo        | 67.4 ms                                                | 63.3 ms: 1.06x faster                                                       |
| nbody                      | 87.0 ms                                                | 81.7 ms: 1.06x faster                                                       |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                                        |
| telco                      | 8.54 ms                                                | 8.07 ms: 1.06x faster                                                       |
| pyflate                    | 471 ms                                                 | 447 ms: 1.05x faster                                                        |
| json_dumps                 | 10.6 ms                                                | 10.1 ms: 1.05x faster                                                       |
| scimark_sor                | 124 ms                                                 | 118 ms: 1.05x faster                                                        |
| async_tree_none_tg         | 321 ms                                                 | 307 ms: 1.04x faster                                                        |
| regex_effbot               | 3.73 ms                                                | 3.59 ms: 1.04x faster                                                       |
| regex_v8                   | 26.2 ms                                                | 25.4 ms: 1.03x faster                                                       |
| logging_format             | 6.40 us                                                | 6.21 us: 1.03x faster                                                       |
| xml_etree_iterparse        | 101 ms                                                 | 98.6 ms: 1.03x faster                                                       |
| pickle_pure_python         | 310 us                                                 | 303 us: 1.03x faster                                                        |
| json_loads                 | 27.2 us                                                | 26.7 us: 1.02x faster                                                       |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                        |
| thrift                     | 809 us                                                 | 797 us: 1.02x faster                                                        |
| scimark_lu                 | 113 ms                                                 | 111 ms: 1.01x faster                                                        |
| deltablue                  | 3.23 ms                                                | 3.19 ms: 1.01x faster                                                       |
| pprint_safe_repr           | 728 ms                                                 | 722 ms: 1.01x faster                                                        |
| logging_simple             | 5.72 us                                                | 5.67 us: 1.01x faster                                                       |
| typing_runtime_protocols   | 165 us                                                 | 164 us: 1.01x faster                                                        |
| unpickle_pure_python       | 216 us                                                 | 215 us: 1.00x faster                                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                                        |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                        |
| regex_dna                  | 218 ms                                                 | 221 ms: 1.01x slower                                                        |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.01x slower                                                       |
| python_startup_no_site     | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 554 ms: 1.02x slower                                                        |
| coverage                   | 84.0 ms                                                | 85.3 ms: 1.02x slower                                                       |
| django_template            | 35.2 ms                                                | 35.8 ms: 1.02x slower                                                       |
| chaos                      | 58.1 ms                                                | 59.2 ms: 1.02x slower                                                       |
| bench_thread_pool          | 822 us                                                 | 839 us: 1.02x slower                                                        |
| html5lib                   | 64.2 ms                                                | 65.6 ms: 1.02x slower                                                       |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                        |
| pprint_pformat             | 1.49 sec                                               | 1.53 sec: 1.02x slower                                                      |
| tornado_http               | 92.4 ms                                                | 95.1 ms: 1.03x slower                                                       |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.05x slower                                                       |
| 2to3                       | 267 ms                                                 | 280 ms: 1.05x slower                                                        |
| sqlglot_normalize          | 108 ms                                                 | 113 ms: 1.05x slower                                                        |
| raytrace                   | 267 ms                                                 | 280 ms: 1.05x slower                                                        |
| async_tree_io              | 842 ms                                                 | 888 ms: 1.05x slower                                                        |
| async_generators           | 436 ms                                                 | 460 ms: 1.05x slower                                                        |
| dulwich_log                | 64.3 ms                                                | 68.3 ms: 1.06x slower                                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.36 ms: 1.07x slower                                                       |
| regex_compile              | 132 ms                                                 | 142 ms: 1.07x slower                                                        |
| sqlglot_transpile          | 1.58 ms                                                | 1.71 ms: 1.08x slower                                                       |
| sqlglot_optimize           | 53.7 ms                                                | 58.7 ms: 1.09x slower                                                       |
| sympy_expand               | 463 ms                                                 | 508 ms: 1.10x slower                                                        |
| genshi_text                | 23.5 ms                                                | 25.8 ms: 1.10x slower                                                       |
| sympy_str                  | 275 ms                                                 | 302 ms: 1.10x slower                                                        |
| nqueens                    | 78.4 ms                                                | 86.5 ms: 1.10x slower                                                       |
| generators                 | 29.0 ms                                                | 32.8 ms: 1.13x slower                                                       |
| hexiom                     | 6.16 ms                                                | 7.05 ms: 1.14x slower                                                       |
| docutils                   | 2.59 sec                                               | 2.97 sec: 1.14x slower                                                      |
| sympy_integrate            | 19.9 ms                                                | 23.1 ms: 1.16x slower                                                       |
| genshi_xml                 | 50.9 ms                                                | 59.0 ms: 1.16x slower                                                       |
| sympy_sum                  | 150 ms                                                 | 176 ms: 1.17x slower                                                        |
| pylint                     | 313 ms                                                 | 376 ms: 1.20x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                |

Benchmark hidden because not significant (4): bench_mp_pool, async_tree_cpu_io_mixed, pycparser, async_tree_io_tg
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240913-3.14.0a0-e2ba0e8-JIT/bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.027x faster
# HPT report

- Reliability score: 80.28% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x