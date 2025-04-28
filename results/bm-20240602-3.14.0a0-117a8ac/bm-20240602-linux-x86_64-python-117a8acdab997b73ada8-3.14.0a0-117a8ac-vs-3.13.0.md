# Results vs. 3.13.0

- fork: python
- ref: 117a8acdab997b73ada8
- machine: linux-x86_64
- commit hash: 117a8ac
- commit date: 2024-06-02
- overall geometric mean: 1.012x slower
- HPT reliability: 93.82%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 265 ms: 1.00x faster                                                  |
| docutils       | 2.58 sec                                               | 2.72 sec: 1.05x slower                                                |
| html5lib       | 63.4 ms                                                | 66.4 ms: 1.05x slower                                                 |
| sphinx         | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                |
| tornado_http   | 91.2 ms                                                | 91.8 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 428 ms: 1.08x faster                                                  |
| async_generators           | 433 ms                                                 | 439 ms: 1.01x slower                                                  |
| coroutines                 | 22.2 ms                                                | 22.9 ms: 1.03x slower                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 601 ms: 1.05x slower                                                  |
| async_tree_none            | 350 ms                                                 | 370 ms: 1.06x slower                                                  |
| async_tree_memoization     | 437 ms                                                 | 462 ms: 1.06x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 592 ms: 1.09x slower                                                  |
| async_tree_io              | 838 ms                                                 | 936 ms: 1.12x slower                                                  |
| async_tree_io_tg           | 861 ms                                                 | 973 ms: 1.13x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x slower                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 77.1 ms: 1.02x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| nbody          | 87.7 ms                                                | 88.5 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.0 ms: 1.22x faster                                                 |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                  |
| regex_effbot   | 3.77 ms                                                | 3.73 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process   | 60.5 ms                                                | 59.1 ms: 1.02x faster                                                 |
| xml_etree_generate  | 86.8 ms                                                | 85.0 ms: 1.02x faster                                                 |
| tomli_loads         | 2.12 sec                                               | 2.13 sec: 1.01x slower                                                |
| xml_etree_parse     | 154 ms                                                 | 156 ms: 1.01x slower                                                  |
| json_loads          | 27.2 us                                                | 27.5 us: 1.01x slower                                                 |
| json_dumps          | 10.1 ms                                                | 10.5 ms: 1.04x slower                                                 |
| xml_etree_iterparse | 101 ms                                                 | 106 ms: 1.04x slower                                                  |
| Geometric mean      | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.91 ms: 1.01x faster                                                 |
| python_startup         | 12.7 ms                                                | 14.2 ms: 1.12x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 23.1 ms: 1.02x slower                                                 |
| django_template | 31.7 ms                                                | 32.5 ms: 1.03x slower                                                 |
| mako            | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8                   | 26.9 ms                                                | 22.0 ms: 1.22x faster                                                 |
| gc_traversal               | 4.90 ms                                                | 4.28 ms: 1.14x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 428 ms: 1.08x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.3 ms: 1.07x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                |
| json                       | 5.32 ms                                                | 5.20 ms: 1.02x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 59.1 ms: 1.02x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 85.0 ms: 1.02x faster                                                 |
| crypto_pyaes               | 74.7 ms                                                | 73.2 ms: 1.02x faster                                                 |
| float                      | 78.7 ms                                                | 77.1 ms: 1.02x faster                                                 |
| mdp                        | 2.54 sec                                               | 2.50 sec: 1.02x faster                                                |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.02x faster                                                  |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                  |
| subparsers                 | 15.5 ms                                                | 15.2 ms: 1.02x faster                                                 |
| scimark_lu                 | 114 ms                                                 | 113 ms: 1.01x faster                                                  |
| pyflate                    | 470 ms                                                 | 464 ms: 1.01x faster                                                  |
| python_startup_no_site     | 7.00 ms                                                | 6.91 ms: 1.01x faster                                                 |
| scimark_fft                | 367 ms                                                 | 363 ms: 1.01x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.73 ms: 1.01x faster                                                 |
| generators                 | 28.8 ms                                                | 28.6 ms: 1.01x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.01x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 3.22 us: 1.01x faster                                                 |
| 2to3                       | 266 ms                                                 | 265 ms: 1.00x faster                                                  |
| deepcopy                   | 354 us                                                 | 353 us: 1.00x faster                                                  |
| comprehensions             | 16.5 us                                                | 16.4 us: 1.00x faster                                                 |
| fannkuch                   | 394 ms                                                 | 393 ms: 1.00x faster                                                  |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                 |
| sympy_expand               | 456 ms                                                 | 458 ms: 1.00x slower                                                  |
| deepcopy_memo              | 38.4 us                                                | 38.6 us: 1.01x slower                                                 |
| logging_simple             | 5.65 us                                                | 5.68 us: 1.01x slower                                                 |
| tornado_http               | 91.2 ms                                                | 91.8 ms: 1.01x slower                                                 |
| tomli_loads                | 2.12 sec                                               | 2.13 sec: 1.01x slower                                                |
| bench_thread_pool          | 818 us                                                 | 824 us: 1.01x slower                                                  |
| chaos                      | 58.0 ms                                                | 58.5 ms: 1.01x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 67.4 ms: 1.01x slower                                                 |
| nbody                      | 87.7 ms                                                | 88.5 ms: 1.01x slower                                                 |
| xml_etree_parse            | 154 ms                                                 | 156 ms: 1.01x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 734 ms: 1.01x slower                                                  |
| many_optionals             | 857 us                                                 | 866 us: 1.01x slower                                                  |
| json_loads                 | 27.2 us                                                | 27.5 us: 1.01x slower                                                 |
| async_generators           | 433 ms                                                 | 439 ms: 1.01x slower                                                  |
| dulwich_log                | 64.6 ms                                                | 65.4 ms: 1.01x slower                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 135 ms: 1.02x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.50 sec: 1.02x slower                                                |
| sphinx                     | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                |
| raytrace                   | 262 ms                                                 | 266 ms: 1.02x slower                                                  |
| go                         | 141 ms                                                 | 143 ms: 1.02x slower                                                  |
| genshi_text                | 22.6 ms                                                | 23.1 ms: 1.02x slower                                                 |
| thrift                     | 800 us                                                 | 819 us: 1.02x slower                                                  |
| django_template            | 31.7 ms                                                | 32.5 ms: 1.03x slower                                                 |
| coroutines                 | 22.2 ms                                                | 22.9 ms: 1.03x slower                                                 |
| logging_silent             | 101 ns                                                 | 105 ns: 1.03x slower                                                  |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 10.5 ms: 1.04x slower                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 106 ms: 1.04x slower                                                  |
| html5lib                   | 63.4 ms                                                | 66.4 ms: 1.05x slower                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 601 ms: 1.05x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.72 sec: 1.05x slower                                                |
| gevent_hub                 | 1.05 ns                                                | 1.11 ns: 1.06x slower                                                 |
| async_tree_none            | 350 ms                                                 | 370 ms: 1.06x slower                                                  |
| async_tree_memoization     | 437 ms                                                 | 462 ms: 1.06x slower                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.96 sec: 1.06x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.60 ms: 1.06x slower                                                 |
| richards                   | 47.5 ms                                                | 50.5 ms: 1.06x slower                                                 |
| richards_super             | 53.7 ms                                                | 57.2 ms: 1.06x slower                                                 |
| scimark_sor                | 122 ms                                                 | 131 ms: 1.07x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 592 ms: 1.09x slower                                                  |
| coverage                   | 82.8 ms                                                | 91.6 ms: 1.11x slower                                                 |
| async_tree_io              | 838 ms                                                 | 936 ms: 1.12x slower                                                  |
| python_startup             | 12.7 ms                                                | 14.2 ms: 1.12x slower                                                 |
| async_tree_io_tg           | 861 ms                                                 | 973 ms: 1.13x slower                                                  |
| k_core                     | 2.37 sec                                               | 3.53 sec: 1.49x slower                                                |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (22): pylint, connected_components, scimark_sparse_mat_mult, genshi_xml, sympy_str, pickle_pure_python, hexiom, spectral_norm, shortest_path, deltablue, regex_compile, nqueens, unpickle_pure_python, typing_runtime_protocols, sympy_integrate, telco, asyncio_websockets, sqlite_synth, logging_format, sqlalchemy_imperative, djangocms, async_tree_none_tg
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
Ignored benchmarks (12) of results/bm-20240602-3.14.0a0-117a8ac/bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.012x slower

# HPT report

- Reliability score: 93.82% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x