# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_exit_leaks
- machine: linux-x86_64
- commit hash: 984ca75
- commit date: 2024-10-01
- overall geometric mean: 1.025x faster
- HPT reliability: 82.09%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 279 ms: 1.05x slower                                                       |
| docutils       | 2.59 sec                                               | 2.92 sec: 1.12x slower                                                     |
| html5lib       | 64.2 ms                                                | 66.2 ms: 1.03x slower                                                      |
| tornado_http   | 92.4 ms                                                | 95.7 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.06x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 391 ms: 1.18x faster                                                       |
| async_tree_none            | 351 ms                                                 | 321 ms: 1.09x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 410 ms: 1.08x faster                                                       |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 554 ms: 1.02x slower                                                       |
| async_tree_io_tg           | 857 ms                                                 | 880 ms: 1.03x slower                                                       |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                                      |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                                       |
| async_tree_io              | 842 ms                                                 | 891 ms: 1.06x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 72.3 ms: 1.10x faster                                                      |
| nbody          | 87.0 ms                                                | 80.5 ms: 1.08x faster                                                      |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.3 ms: 1.08x faster                                                      |
| regex_effbot   | 3.73 ms                                                | 3.65 ms: 1.02x faster                                                      |
| regex_dna      | 218 ms                                                 | 222 ms: 1.01x slower                                                       |
| regex_compile  | 132 ms                                                 | 143 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                  | 1.00x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 77.7 ms: 1.12x faster                                                      |
| tomli_loads          | 2.14 sec                                               | 1.93 sec: 1.11x faster                                                     |
| xml_etree_process    | 60.6 ms                                                | 55.2 ms: 1.10x faster                                                      |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 101 ms                                                 | 97.5 ms: 1.04x faster                                                      |
| json_dumps           | 10.6 ms                                                | 10.3 ms: 1.02x faster                                                      |
| json_loads           | 27.2 us                                                | 26.7 us: 1.02x faster                                                      |
| unpickle_pure_python | 216 us                                                 | 213 us: 1.01x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                      |
| python_startup_no_site | 6.96 ms                                                | 7.06 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.87 ms: 1.12x faster                                                      |
| django_template | 35.2 ms                                                | 36.0 ms: 1.03x slower                                                      |
| genshi_text     | 23.5 ms                                                | 25.3 ms: 1.08x slower                                                      |
| genshi_xml      | 50.9 ms                                                | 59.2 ms: 1.16x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 27.0 us: 1.45x faster                                                      |
| create_gc_cycles           | 2.41 ms                                                | 1.73 ms: 1.39x faster                                                      |
| deepcopy                   | 358 us                                                 | 271 us: 1.32x faster                                                       |
| richards_super             | 54.9 ms                                                | 45.1 ms: 1.22x faster                                                      |
| richards                   | 48.7 ms                                                | 40.0 ms: 1.22x faster                                                      |
| deepcopy_reduce            | 3.20 us                                                | 2.67 us: 1.20x faster                                                      |
| scimark_fft                | 364 ms                                                 | 307 ms: 1.19x faster                                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 391 ms: 1.18x faster                                                       |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                      |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.37 ms: 1.15x faster                                                      |
| crypto_pyaes               | 75.3 ms                                                | 65.7 ms: 1.15x faster                                                      |
| telco                      | 8.54 ms                                                | 7.49 ms: 1.14x faster                                                      |
| mako                       | 11.1 ms                                                | 9.87 ms: 1.12x faster                                                      |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                       |
| pathlib                    | 17.5 ms                                                | 15.7 ms: 1.12x faster                                                      |
| xml_etree_generate         | 86.7 ms                                                | 77.7 ms: 1.12x faster                                                      |
| tomli_loads                | 2.14 sec                                               | 1.93 sec: 1.11x faster                                                     |
| xml_etree_process          | 60.6 ms                                                | 55.2 ms: 1.10x faster                                                      |
| float                      | 79.2 ms                                                | 72.3 ms: 1.10x faster                                                      |
| gc_traversal               | 4.37 ms                                                | 3.99 ms: 1.09x faster                                                      |
| async_tree_none            | 351 ms                                                 | 321 ms: 1.09x faster                                                       |
| go                         | 144 ms                                                 | 132 ms: 1.09x faster                                                       |
| nbody                      | 87.0 ms                                                | 80.5 ms: 1.08x faster                                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 62.5 ms: 1.08x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 410 ms: 1.08x faster                                                       |
| regex_v8                   | 26.2 ms                                                | 24.3 ms: 1.08x faster                                                      |
| fannkuch                   | 404 ms                                                 | 376 ms: 1.08x faster                                                       |
| bpe_tokeniser              | 4.75 sec                                               | 4.42 sec: 1.07x faster                                                     |
| mdp                        | 2.72 sec                                               | 2.54 sec: 1.07x faster                                                     |
| xml_etree_parse            | 156 ms                                                 | 145 ms: 1.07x faster                                                       |
| json                       | 5.36 ms                                                | 5.02 ms: 1.07x faster                                                      |
| scimark_sor                | 124 ms                                                 | 117 ms: 1.06x faster                                                       |
| logging_format             | 6.40 us                                                | 6.08 us: 1.05x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 97.5 ms: 1.04x faster                                                      |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                                     |
| scimark_lu                 | 113 ms                                                 | 109 ms: 1.03x faster                                                       |
| logging_simple             | 5.72 us                                                | 5.54 us: 1.03x faster                                                      |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.02x faster                                                       |
| regex_effbot               | 3.73 ms                                                | 3.65 ms: 1.02x faster                                                      |
| json_dumps                 | 10.6 ms                                                | 10.3 ms: 1.02x faster                                                      |
| json_loads                 | 27.2 us                                                | 26.7 us: 1.02x faster                                                      |
| pyflate                    | 471 ms                                                 | 462 ms: 1.02x faster                                                       |
| unpickle_pure_python       | 216 us                                                 | 213 us: 1.01x faster                                                       |
| deltablue                  | 3.23 ms                                                | 3.21 ms: 1.01x faster                                                      |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                       |
| pprint_safe_repr           | 728 ms                                                 | 735 ms: 1.01x slower                                                       |
| python_startup_no_site     | 6.96 ms                                                | 7.06 ms: 1.01x slower                                                      |
| regex_dna                  | 218 ms                                                 | 222 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 554 ms: 1.02x slower                                                       |
| coverage                   | 84.0 ms                                                | 85.3 ms: 1.02x slower                                                      |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                      |
| django_template            | 35.2 ms                                                | 36.0 ms: 1.03x slower                                                      |
| async_tree_io_tg           | 857 ms                                                 | 880 ms: 1.03x slower                                                       |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                                      |
| logging_silent             | 102 ns                                                 | 105 ns: 1.03x slower                                                       |
| html5lib                   | 64.2 ms                                                | 66.2 ms: 1.03x slower                                                      |
| pprint_pformat             | 1.49 sec                                               | 1.54 sec: 1.03x slower                                                     |
| chaos                      | 58.1 ms                                                | 60.0 ms: 1.03x slower                                                      |
| raytrace                   | 267 ms                                                 | 276 ms: 1.04x slower                                                       |
| tornado_http               | 92.4 ms                                                | 95.7 ms: 1.04x slower                                                      |
| 2to3                       | 267 ms                                                 | 279 ms: 1.05x slower                                                       |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                                       |
| dulwich_log                | 64.3 ms                                                | 67.8 ms: 1.05x slower                                                      |
| async_tree_io              | 842 ms                                                 | 891 ms: 1.06x slower                                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.35 ms: 1.06x slower                                                      |
| sqlglot_transpile          | 1.58 ms                                                | 1.70 ms: 1.07x slower                                                      |
| genshi_text                | 23.5 ms                                                | 25.3 ms: 1.08x slower                                                      |
| regex_compile              | 132 ms                                                 | 143 ms: 1.08x slower                                                       |
| sqlglot_normalize          | 108 ms                                                 | 117 ms: 1.08x slower                                                       |
| bench_thread_pool          | 822 us                                                 | 894 us: 1.09x slower                                                       |
| sympy_expand               | 463 ms                                                 | 508 ms: 1.10x slower                                                       |
| sympy_str                  | 275 ms                                                 | 305 ms: 1.11x slower                                                       |
| hexiom                     | 6.16 ms                                                | 6.92 ms: 1.12x slower                                                      |
| docutils                   | 2.59 sec                                               | 2.92 sec: 1.12x slower                                                     |
| sqlglot_optimize           | 53.7 ms                                                | 60.5 ms: 1.13x slower                                                      |
| nqueens                    | 78.4 ms                                                | 88.6 ms: 1.13x slower                                                      |
| genshi_xml                 | 50.9 ms                                                | 59.2 ms: 1.16x slower                                                      |
| sympy_sum                  | 150 ms                                                 | 176 ms: 1.17x slower                                                       |
| sympy_integrate            | 19.9 ms                                                | 23.5 ms: 1.18x slower                                                      |
| pylint                     | 313 ms                                                 | 374 ms: 1.20x slower                                                       |
| generators                 | 29.0 ms                                                | 34.9 ms: 1.21x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 60.7 ms: 2.53x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (5): async_tree_none_tg, pickle_pure_python, async_tree_cpu_io_mixed, thrift, typing_runtime_protocols
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241001-3.14.0a0-984ca75-JIT/bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.025x faster
# HPT report

- Reliability score: 82.09% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.96x