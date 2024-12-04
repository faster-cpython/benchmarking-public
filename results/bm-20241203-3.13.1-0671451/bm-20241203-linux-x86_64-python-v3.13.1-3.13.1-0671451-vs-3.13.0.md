# Results vs. 3.13.0

- fork: python
- ref: v3.13.1
- machine: linux-x86_64
- commit hash: 0671451
- commit date: 2024-12-03
- overall geometric mean: 1.003x faster
- HPT reliability: 86.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-linux-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| chameleon      | 6.94 ms                                                | 7.09 ms: 1.02x slower                                  |
| docutils       | 2.59 sec                                               | 2.61 sec: 1.01x slower                                 |
| html5lib       | 64.2 ms                                                | 66.0 ms: 1.03x slower                                  |
| tornado_http   | 92.4 ms                                                | 91.4 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-linux-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_none_tg         | 321 ms                                                 | 311 ms: 1.03x faster                                   |
| async_tree_memoization_tg  | 464 ms                                                 | 452 ms: 1.03x faster                                   |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 595 ms: 1.09x slower                                   |
| Geometric mean             | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (8): async_tree_io, async_tree_none, async_tree_cpu_io_mixed, coroutines, asyncio_websockets, async_tree_io_tg, async_generators, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-linux-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 79.2 ms                                                | 78.2 ms: 1.01x faster                                  |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                   |
| nbody          | 87.0 ms                                                | 90.5 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-linux-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.49 ms: 1.07x faster                                  |
| regex_compile  | 132 ms                                                 | 131 ms: 1.01x faster                                   |
| regex_v8       | 26.2 ms                                                | 26.6 ms: 1.02x slower                                  |
| regex_dna      | 218 ms                                                 | 225 ms: 1.03x slower                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-linux-x86_64-python-v3.13.1-3.13.1-0671451 |
|--------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| tomli_loads        | 2.14 sec                                               | 2.06 sec: 1.04x faster                                 |
| json_dumps         | 10.6 ms                                                | 10.3 ms: 1.02x faster                                  |
| pickle_pure_python | 310 us                                                 | 307 us: 1.01x faster                                   |
| xml_etree_process  | 60.6 ms                                                | 60.0 ms: 1.01x faster                                  |
| xml_etree_generate | 86.7 ms                                                | 86.2 ms: 1.01x faster                                  |
| Geometric mean     | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_iterparse, unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-linux-x86_64-python-v3.13.1-3.13.1-0671451 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 6.97 ms: 1.00x slower                                  |
| python_startup         | 12.5 ms                                                | 12.7 ms: 1.02x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-linux-x86_64-python-v3.13.1-3.13.1-0671451 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 35.2 ms                                                | 31.4 ms: 1.12x faster                                  |
| genshi_text     | 23.5 ms                                                | 22.6 ms: 1.04x faster                                  |
| genshi_xml      | 50.9 ms                                                | 50.1 ms: 1.02x faster                                  |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-linux-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template            | 35.2 ms                                                | 31.4 ms: 1.12x faster                                  |
| mdp                        | 2.72 sec                                               | 2.54 sec: 1.07x faster                                 |
| regex_effbot               | 3.73 ms                                                | 3.49 ms: 1.07x faster                                  |
| genshi_text                | 23.5 ms                                                | 22.6 ms: 1.04x faster                                  |
| tomli_loads                | 2.14 sec                                               | 2.06 sec: 1.04x faster                                 |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                 |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                   |
| async_tree_none_tg         | 321 ms                                                 | 311 ms: 1.03x faster                                   |
| async_tree_memoization_tg  | 464 ms                                                 | 452 ms: 1.03x faster                                   |
| logging_format             | 6.40 us                                                | 6.25 us: 1.02x faster                                  |
| json_dumps                 | 10.6 ms                                                | 10.3 ms: 1.02x faster                                  |
| genshi_xml                 | 50.9 ms                                                | 50.1 ms: 1.02x faster                                  |
| crypto_pyaes               | 75.3 ms                                                | 74.1 ms: 1.02x faster                                  |
| go                         | 144 ms                                                 | 142 ms: 1.02x faster                                   |
| scimark_fft                | 364 ms                                                 | 359 ms: 1.01x faster                                   |
| deltablue                  | 3.23 ms                                                | 3.19 ms: 1.01x faster                                  |
| float                      | 79.2 ms                                                | 78.2 ms: 1.01x faster                                  |
| typing_runtime_protocols   | 165 us                                                 | 163 us: 1.01x faster                                   |
| logging_simple             | 5.72 us                                                | 5.65 us: 1.01x faster                                  |
| pickle_pure_python         | 310 us                                                 | 307 us: 1.01x faster                                   |
| tornado_http               | 92.4 ms                                                | 91.4 ms: 1.01x faster                                  |
| xml_etree_process          | 60.6 ms                                                | 60.0 ms: 1.01x faster                                  |
| raytrace                   | 267 ms                                                 | 264 ms: 1.01x faster                                   |
| regex_compile              | 132 ms                                                 | 131 ms: 1.01x faster                                   |
| scimark_monte_carlo        | 67.4 ms                                                | 66.9 ms: 1.01x faster                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.01x faster                                   |
| thrift                     | 809 us                                                 | 803 us: 1.01x faster                                   |
| deepcopy                   | 358 us                                                 | 356 us: 1.01x faster                                   |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.0 ms: 1.01x faster                                  |
| richards                   | 48.7 ms                                                | 48.4 ms: 1.01x faster                                  |
| pyflate                    | 471 ms                                                 | 468 ms: 1.01x faster                                   |
| xml_etree_generate         | 86.7 ms                                                | 86.2 ms: 1.01x faster                                  |
| generators                 | 29.0 ms                                                | 28.8 ms: 1.01x faster                                  |
| bpe_tokeniser              | 4.75 sec                                               | 4.72 sec: 1.01x faster                                 |
| bench_thread_pool          | 822 us                                                 | 818 us: 1.00x faster                                   |
| sqlglot_optimize           | 53.7 ms                                                | 53.5 ms: 1.00x faster                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.27 ms: 1.00x faster                                  |
| python_startup_no_site     | 6.96 ms                                                | 6.97 ms: 1.00x slower                                  |
| sympy_integrate            | 19.9 ms                                                | 20.0 ms: 1.00x slower                                  |
| hexiom                     | 6.16 ms                                                | 6.19 ms: 1.00x slower                                  |
| nqueens                    | 78.4 ms                                                | 78.8 ms: 1.01x slower                                  |
| deepcopy_memo              | 39.1 us                                                | 39.3 us: 1.01x slower                                  |
| docutils                   | 2.59 sec                                               | 2.61 sec: 1.01x slower                                 |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                   |
| mako                       | 11.1 ms                                                | 11.2 ms: 1.01x slower                                  |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                   |
| gc_traversal               | 4.37 ms                                                | 4.41 ms: 1.01x slower                                  |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.09 ms: 1.01x slower                                  |
| shortest_path              | 481 ms                                                 | 485 ms: 1.01x slower                                   |
| scimark_sor                | 124 ms                                                 | 125 ms: 1.01x slower                                   |
| create_gc_cycles           | 2.41 ms                                                | 2.43 ms: 1.01x slower                                  |
| dulwich_log                | 64.3 ms                                                | 65.0 ms: 1.01x slower                                  |
| coverage                   | 84.0 ms                                                | 84.9 ms: 1.01x slower                                  |
| logging_silent             | 102 ns                                                 | 103 ns: 1.01x slower                                   |
| regex_v8                   | 26.2 ms                                                | 26.6 ms: 1.02x slower                                  |
| python_startup             | 12.5 ms                                                | 12.7 ms: 1.02x slower                                  |
| pprint_pformat             | 1.49 sec                                               | 1.52 sec: 1.02x slower                                 |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                  |
| scimark_lu                 | 113 ms                                                 | 115 ms: 1.02x slower                                   |
| chameleon                  | 6.94 ms                                                | 7.09 ms: 1.02x slower                                  |
| pprint_safe_repr           | 728 ms                                                 | 745 ms: 1.02x slower                                   |
| gevent_hub                 | 1.06 ns                                                | 1.09 ns: 1.03x slower                                  |
| html5lib                   | 64.2 ms                                                | 66.0 ms: 1.03x slower                                  |
| regex_dna                  | 218 ms                                                 | 225 ms: 1.03x slower                                   |
| nbody                      | 87.0 ms                                                | 90.5 ms: 1.04x slower                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 595 ms: 1.09x slower                                   |
| Geometric mean             | (ref)                                                  | 1.00x faster                                           |

Benchmark hidden because not significant (30): async_tree_io, fannkuch, xml_etree_parse, async_tree_none, pathlib, telco, async_tree_cpu_io_mixed, sqlglot_normalize, k_core, meteor_contest, coroutines, json, sqlglot_transpile, sympy_expand, xml_etree_iterparse, asyncio_websockets, 2to3, bench_mp_pool, deepcopy_reduce, unpickle_pure_python, chaos, async_tree_io_tg, async_generators, connected_components, pylint, json_loads, sympy_str, richards_super, sphinx, async_tree_memoization
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: mypy2
Ignored benchmarks (5) of results/bm-20241203-3.13.1-0671451/bm-20241203-linux-x86_64-python-v3.13.1-3.13.1-0671451.json: djangocms, gunicorn, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 86.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x