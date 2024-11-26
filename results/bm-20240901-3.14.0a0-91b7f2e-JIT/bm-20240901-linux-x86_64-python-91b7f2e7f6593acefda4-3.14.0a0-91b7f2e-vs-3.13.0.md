# Results vs. 3.13.0

- fork: python
- ref: 91b7f2e7f6593acefda4
- machine: linux-x86_64
- commit hash: 91b7f2e
- commit date: 2024-09-01
- overall geometric mean: 1.031x faster
- HPT reliability: 95.62%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 276 ms: 1.04x slower                                                  |
| docutils       | 2.59 sec                                               | 2.96 sec: 1.14x slower                                                |
| html5lib       | 64.2 ms                                                | 64.7 ms: 1.01x slower                                                 |
| tornado_http   | 92.4 ms                                                | 94.4 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 406 ms: 1.14x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 401 ms: 1.10x faster                                                  |
| async_tree_none            | 351 ms                                                 | 326 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 554 ms: 1.04x faster                                                  |
| async_tree_none_tg         | 321 ms                                                 | 310 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 537 ms: 1.02x faster                                                  |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                  |
| async_generators           | 436 ms                                                 | 455 ms: 1.04x slower                                                  |
| async_tree_io_tg           | 857 ms                                                 | 899 ms: 1.05x slower                                                  |
| async_tree_io              | 842 ms                                                 | 933 ms: 1.11x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 70.1 ms: 1.13x faster                                                 |
| nbody          | 87.0 ms                                                | 79.8 ms: 1.09x faster                                                 |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.0 ms: 1.09x faster                                                 |
| regex_effbot   | 3.73 ms                                                | 3.52 ms: 1.06x faster                                                 |
| regex_dna      | 218 ms                                                 | 217 ms: 1.01x faster                                                  |
| regex_compile  | 132 ms                                                 | 141 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads         | 2.14 sec                                               | 1.91 sec: 1.12x faster                                                |
| xml_etree_generate  | 86.7 ms                                                | 77.6 ms: 1.12x faster                                                 |
| xml_etree_process   | 60.6 ms                                                | 55.1 ms: 1.10x faster                                                 |
| xml_etree_parse     | 156 ms                                                 | 145 ms: 1.07x faster                                                  |
| xml_etree_iterparse | 101 ms                                                 | 98.3 ms: 1.03x faster                                                 |
| pickle_pure_python  | 310 us                                                 | 304 us: 1.02x faster                                                  |
| json_dumps          | 10.6 ms                                                | 10.4 ms: 1.01x faster                                                 |
| json_loads          | 27.2 us                                                | 28.6 us: 1.05x slower                                                 |
| Geometric mean      | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                 |
| python_startup_no_site | 6.96 ms                                                | 7.15 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.97 ms: 1.11x faster                                                 |
| django_template | 35.2 ms                                                | 36.3 ms: 1.03x slower                                                 |
| genshi_text     | 23.5 ms                                                | 24.9 ms: 1.06x slower                                                 |
| genshi_xml      | 50.9 ms                                                | 58.3 ms: 1.14x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 26.7 us: 1.47x faster                                                 |
| create_gc_cycles           | 2.41 ms                                                | 1.75 ms: 1.37x faster                                                 |
| deepcopy                   | 358 us                                                 | 267 us: 1.34x faster                                                  |
| richards                   | 48.7 ms                                                | 39.3 ms: 1.24x faster                                                 |
| gc_traversal               | 4.37 ms                                                | 3.56 ms: 1.23x faster                                                 |
| deepcopy_reduce            | 3.20 us                                                | 2.65 us: 1.21x faster                                                 |
| richards_super             | 54.9 ms                                                | 45.4 ms: 1.21x faster                                                 |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                 |
| scimark_fft                | 364 ms                                                 | 309 ms: 1.18x faster                                                  |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.34 ms: 1.16x faster                                                 |
| spectral_norm              | 115 ms                                                 | 99.9 ms: 1.15x faster                                                 |
| crypto_pyaes               | 75.3 ms                                                | 65.7 ms: 1.15x faster                                                 |
| async_tree_memoization_tg  | 464 ms                                                 | 406 ms: 1.14x faster                                                  |
| float                      | 79.2 ms                                                | 70.1 ms: 1.13x faster                                                 |
| tomli_loads                | 2.14 sec                                               | 1.91 sec: 1.12x faster                                                |
| xml_etree_generate         | 86.7 ms                                                | 77.6 ms: 1.12x faster                                                 |
| mako                       | 11.1 ms                                                | 9.97 ms: 1.11x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 401 ms: 1.10x faster                                                  |
| xml_etree_process          | 60.6 ms                                                | 55.1 ms: 1.10x faster                                                 |
| pathlib                    | 17.5 ms                                                | 16.0 ms: 1.10x faster                                                 |
| go                         | 144 ms                                                 | 131 ms: 1.09x faster                                                  |
| regex_v8                   | 26.2 ms                                                | 24.0 ms: 1.09x faster                                                 |
| nbody                      | 87.0 ms                                                | 79.8 ms: 1.09x faster                                                 |
| fannkuch                   | 404 ms                                                 | 372 ms: 1.09x faster                                                  |
| telco                      | 8.54 ms                                                | 7.93 ms: 1.08x faster                                                 |
| async_tree_none            | 351 ms                                                 | 326 ms: 1.08x faster                                                  |
| scimark_monte_carlo        | 67.4 ms                                                | 62.9 ms: 1.07x faster                                                 |
| xml_etree_parse            | 156 ms                                                 | 145 ms: 1.07x faster                                                  |
| bpe_tokeniser              | 4.75 sec                                               | 4.43 sec: 1.07x faster                                                |
| mdp                        | 2.72 sec                                               | 2.55 sec: 1.07x faster                                                |
| scimark_sor                | 124 ms                                                 | 116 ms: 1.07x faster                                                  |
| regex_effbot               | 3.73 ms                                                | 3.52 ms: 1.06x faster                                                 |
| logging_format             | 6.40 us                                                | 6.07 us: 1.05x faster                                                 |
| pyflate                    | 471 ms                                                 | 449 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 554 ms: 1.04x faster                                                  |
| logging_simple             | 5.72 us                                                | 5.51 us: 1.04x faster                                                 |
| async_tree_none_tg         | 321 ms                                                 | 310 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 98.3 ms: 1.03x faster                                                 |
| thrift                     | 809 us                                                 | 786 us: 1.03x faster                                                  |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.02x faster                                                  |
| pickle_pure_python         | 310 us                                                 | 304 us: 1.02x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 537 ms: 1.02x faster                                                  |
| pprint_safe_repr           | 728 ms                                                 | 718 ms: 1.01x faster                                                  |
| pprint_pformat             | 1.49 sec                                               | 1.47 sec: 1.01x faster                                                |
| deltablue                  | 3.23 ms                                                | 3.19 ms: 1.01x faster                                                 |
| json_dumps                 | 10.6 ms                                                | 10.4 ms: 1.01x faster                                                 |
| scimark_lu                 | 113 ms                                                 | 111 ms: 1.01x faster                                                  |
| regex_dna                  | 218 ms                                                 | 217 ms: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 185 ms: 1.01x faster                                                  |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                  |
| chaos                      | 58.1 ms                                                | 58.5 ms: 1.01x slower                                                 |
| html5lib                   | 64.2 ms                                                | 64.7 ms: 1.01x slower                                                 |
| bench_thread_pool          | 822 us                                                 | 833 us: 1.01x slower                                                  |
| coverage                   | 84.0 ms                                                | 85.4 ms: 1.02x slower                                                 |
| tornado_http               | 92.4 ms                                                | 94.4 ms: 1.02x slower                                                 |
| python_startup_no_site     | 6.96 ms                                                | 7.15 ms: 1.03x slower                                                 |
| raytrace                   | 267 ms                                                 | 275 ms: 1.03x slower                                                  |
| django_template            | 35.2 ms                                                | 36.3 ms: 1.03x slower                                                 |
| 2to3                       | 267 ms                                                 | 276 ms: 1.04x slower                                                  |
| async_generators           | 436 ms                                                 | 455 ms: 1.04x slower                                                  |
| async_tree_io_tg           | 857 ms                                                 | 899 ms: 1.05x slower                                                  |
| json_loads                 | 27.2 us                                                | 28.6 us: 1.05x slower                                                 |
| sqlglot_normalize          | 108 ms                                                 | 113 ms: 1.05x slower                                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.05x slower                                                 |
| genshi_text                | 23.5 ms                                                | 24.9 ms: 1.06x slower                                                 |
| dulwich_log                | 64.3 ms                                                | 68.2 ms: 1.06x slower                                                 |
| sqlglot_transpile          | 1.58 ms                                                | 1.69 ms: 1.07x slower                                                 |
| regex_compile              | 132 ms                                                 | 141 ms: 1.07x slower                                                  |
| nqueens                    | 78.4 ms                                                | 85.1 ms: 1.09x slower                                                 |
| sqlglot_optimize           | 53.7 ms                                                | 58.4 ms: 1.09x slower                                                 |
| sympy_expand               | 463 ms                                                 | 507 ms: 1.09x slower                                                  |
| sympy_str                  | 275 ms                                                 | 301 ms: 1.09x slower                                                  |
| async_tree_io              | 842 ms                                                 | 933 ms: 1.11x slower                                                  |
| hexiom                     | 6.16 ms                                                | 6.86 ms: 1.11x slower                                                 |
| docutils                   | 2.59 sec                                               | 2.96 sec: 1.14x slower                                                |
| generators                 | 29.0 ms                                                | 33.1 ms: 1.14x slower                                                 |
| genshi_xml                 | 50.9 ms                                                | 58.3 ms: 1.14x slower                                                 |
| sympy_integrate            | 19.9 ms                                                | 22.8 ms: 1.15x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 173 ms: 1.15x slower                                                  |
| pylint                     | 313 ms                                                 | 372 ms: 1.19x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (7): unpickle_pure_python, typing_runtime_protocols, json, bench_mp_pool, logging_silent, coroutines, comprehensions
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240901-3.14.0a0-91b7f2e-JIT/bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.031x faster
# HPT report

- Reliability score: 95.62% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x