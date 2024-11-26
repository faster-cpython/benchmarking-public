# Results vs. 3.13.0

- fork: brandtbucher
- ref: decref_escapes
- machine: linux-x86_64
- commit hash: 4711506
- commit date: 2024-09-19
- overall geometric mean: 1.027x faster
- HPT reliability: 77.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 277 ms: 1.04x slower                                                  |
| docutils       | 2.59 sec                                               | 2.97 sec: 1.15x slower                                                |
| html5lib       | 64.2 ms                                                | 63.8 ms: 1.01x faster                                                 |
| tornado_http   | 92.4 ms                                                | 95.1 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 389 ms: 1.19x faster                                                  |
| async_tree_none            | 351 ms                                                 | 319 ms: 1.10x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 403 ms: 1.10x faster                                                  |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                  |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 555 ms: 1.02x slower                                                  |
| async_tree_io_tg           | 857 ms                                                 | 876 ms: 1.02x slower                                                  |
| async_generators           | 436 ms                                                 | 451 ms: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 70.7 ms: 1.12x faster                                                 |
| nbody          | 87.0 ms                                                | 80.2 ms: 1.08x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.1 ms: 1.04x faster                                                 |
| regex_effbot   | 3.73 ms                                                | 3.68 ms: 1.01x faster                                                 |
| regex_dna      | 218 ms                                                 | 224 ms: 1.03x slower                                                  |
| regex_compile  | 132 ms                                                 | 142 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate  | 86.7 ms                                                | 77.9 ms: 1.11x faster                                                 |
| xml_etree_process   | 60.6 ms                                                | 54.6 ms: 1.11x faster                                                 |
| tomli_loads         | 2.14 sec                                               | 1.95 sec: 1.10x faster                                                |
| xml_etree_parse     | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| xml_etree_iterparse | 101 ms                                                 | 98.0 ms: 1.03x faster                                                 |
| json_dumps          | 10.6 ms                                                | 10.3 ms: 1.03x faster                                                 |
| pickle_pure_python  | 310 us                                                 | 305 us: 1.02x faster                                                  |
| json_loads          | 27.2 us                                                | 27.5 us: 1.01x slower                                                 |
| Geometric mean      | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                 |
| python_startup_no_site | 6.96 ms                                                | 7.08 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.97 ms: 1.11x faster                                                 |
| django_template | 35.2 ms                                                | 35.4 ms: 1.01x slower                                                 |
| genshi_text     | 23.5 ms                                                | 24.5 ms: 1.04x slower                                                 |
| genshi_xml      | 50.9 ms                                                | 58.0 ms: 1.14x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 26.9 us: 1.45x faster                                                 |
| create_gc_cycles           | 2.41 ms                                                | 1.75 ms: 1.37x faster                                                 |
| deepcopy                   | 358 us                                                 | 263 us: 1.36x faster                                                  |
| richards                   | 48.7 ms                                                | 39.9 ms: 1.22x faster                                                 |
| deepcopy_reduce            | 3.20 us                                                | 2.66 us: 1.21x faster                                                 |
| richards_super             | 54.9 ms                                                | 45.6 ms: 1.20x faster                                                 |
| async_tree_memoization_tg  | 464 ms                                                 | 389 ms: 1.19x faster                                                  |
| python_startup             | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                 |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.29 ms: 1.18x faster                                                 |
| scimark_fft                | 364 ms                                                 | 310 ms: 1.18x faster                                                  |
| gc_traversal               | 4.37 ms                                                | 3.83 ms: 1.14x faster                                                 |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                  |
| crypto_pyaes               | 75.3 ms                                                | 67.2 ms: 1.12x faster                                                 |
| float                      | 79.2 ms                                                | 70.7 ms: 1.12x faster                                                 |
| xml_etree_generate         | 86.7 ms                                                | 77.9 ms: 1.11x faster                                                 |
| xml_etree_process          | 60.6 ms                                                | 54.6 ms: 1.11x faster                                                 |
| mako                       | 11.1 ms                                                | 9.97 ms: 1.11x faster                                                 |
| pathlib                    | 17.5 ms                                                | 15.9 ms: 1.10x faster                                                 |
| async_tree_none            | 351 ms                                                 | 319 ms: 1.10x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 403 ms: 1.10x faster                                                  |
| tomli_loads                | 2.14 sec                                               | 1.95 sec: 1.10x faster                                                |
| go                         | 144 ms                                                 | 132 ms: 1.09x faster                                                  |
| nbody                      | 87.0 ms                                                | 80.2 ms: 1.08x faster                                                 |
| fannkuch                   | 404 ms                                                 | 375 ms: 1.08x faster                                                  |
| telco                      | 8.54 ms                                                | 7.94 ms: 1.08x faster                                                 |
| scimark_monte_carlo        | 67.4 ms                                                | 62.7 ms: 1.08x faster                                                 |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| bpe_tokeniser              | 4.75 sec                                               | 4.47 sec: 1.06x faster                                                |
| scimark_sor                | 124 ms                                                 | 117 ms: 1.06x faster                                                  |
| regex_v8                   | 26.2 ms                                                | 25.1 ms: 1.04x faster                                                 |
| json                       | 5.36 ms                                                | 5.14 ms: 1.04x faster                                                 |
| logging_format             | 6.40 us                                                | 6.13 us: 1.04x faster                                                 |
| pyflate                    | 471 ms                                                 | 451 ms: 1.04x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 98.0 ms: 1.03x faster                                                 |
| typing_runtime_protocols   | 165 us                                                 | 160 us: 1.03x faster                                                  |
| json_dumps                 | 10.6 ms                                                | 10.3 ms: 1.03x faster                                                 |
| scimark_lu                 | 113 ms                                                 | 110 ms: 1.02x faster                                                  |
| thrift                     | 809 us                                                 | 794 us: 1.02x faster                                                  |
| pickle_pure_python         | 310 us                                                 | 305 us: 1.02x faster                                                  |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.01x faster                                                  |
| regex_effbot               | 3.73 ms                                                | 3.68 ms: 1.01x faster                                                 |
| logging_simple             | 5.72 us                                                | 5.65 us: 1.01x faster                                                 |
| mdp                        | 2.72 sec                                               | 2.70 sec: 1.01x faster                                                |
| deltablue                  | 3.23 ms                                                | 3.21 ms: 1.01x faster                                                 |
| html5lib                   | 64.2 ms                                                | 63.8 ms: 1.01x faster                                                 |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| coverage                   | 84.0 ms                                                | 84.5 ms: 1.01x slower                                                 |
| django_template            | 35.2 ms                                                | 35.4 ms: 1.01x slower                                                 |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                  |
| json_loads                 | 27.2 us                                                | 27.5 us: 1.01x slower                                                 |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 555 ms: 1.02x slower                                                  |
| python_startup_no_site     | 6.96 ms                                                | 7.08 ms: 1.02x slower                                                 |
| logging_silent             | 102 ns                                                 | 103 ns: 1.02x slower                                                  |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                 |
| bench_thread_pool          | 822 us                                                 | 838 us: 1.02x slower                                                  |
| async_tree_io_tg           | 857 ms                                                 | 876 ms: 1.02x slower                                                  |
| regex_dna                  | 218 ms                                                 | 224 ms: 1.03x slower                                                  |
| tornado_http               | 92.4 ms                                                | 95.1 ms: 1.03x slower                                                 |
| async_generators           | 436 ms                                                 | 451 ms: 1.04x slower                                                  |
| 2to3                       | 267 ms                                                 | 277 ms: 1.04x slower                                                  |
| genshi_text                | 23.5 ms                                                | 24.5 ms: 1.04x slower                                                 |
| pprint_safe_repr           | 728 ms                                                 | 761 ms: 1.05x slower                                                  |
| chaos                      | 58.1 ms                                                | 60.8 ms: 1.05x slower                                                 |
| pprint_pformat             | 1.49 sec                                               | 1.56 sec: 1.05x slower                                                |
| raytrace                   | 267 ms                                                 | 280 ms: 1.05x slower                                                  |
| sqlglot_normalize          | 108 ms                                                 | 113 ms: 1.05x slower                                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.05x slower                                                 |
| dulwich_log                | 64.3 ms                                                | 68.3 ms: 1.06x slower                                                 |
| sqlglot_transpile          | 1.58 ms                                                | 1.69 ms: 1.06x slower                                                 |
| regex_compile              | 132 ms                                                 | 142 ms: 1.07x slower                                                  |
| sqlglot_optimize           | 53.7 ms                                                | 57.9 ms: 1.08x slower                                                 |
| sympy_str                  | 275 ms                                                 | 299 ms: 1.09x slower                                                  |
| sympy_expand               | 463 ms                                                 | 504 ms: 1.09x slower                                                  |
| nqueens                    | 78.4 ms                                                | 87.9 ms: 1.12x slower                                                 |
| hexiom                     | 6.16 ms                                                | 6.98 ms: 1.13x slower                                                 |
| genshi_xml                 | 50.9 ms                                                | 58.0 ms: 1.14x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 172 ms: 1.14x slower                                                  |
| generators                 | 29.0 ms                                                | 33.1 ms: 1.14x slower                                                 |
| docutils                   | 2.59 sec                                               | 2.97 sec: 1.15x slower                                                |
| sympy_integrate            | 19.9 ms                                                | 22.8 ms: 1.15x slower                                                 |
| pylint                     | 313 ms                                                 | 374 ms: 1.20x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_cpu_io_mixed, bench_mp_pool, unpickle_pure_python, pycparser, async_tree_io
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240919-3.14.0a0-4711506-JIT/bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.027x faster
# HPT report

- Reliability score: 77.72% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x