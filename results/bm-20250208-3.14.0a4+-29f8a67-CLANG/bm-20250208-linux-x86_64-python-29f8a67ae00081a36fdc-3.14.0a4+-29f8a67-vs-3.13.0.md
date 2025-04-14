# Results vs. 3.13.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-x86_64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.080x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 247 ms: 1.08x faster                                                   |
| docutils       | 2.58 sec                                               | 2.56 sec: 1.01x faster                                                 |
| html5lib       | 63.4 ms                                                | 60.3 ms: 1.05x faster                                                  |
| sphinx         | 1.03 sec                                               | 978 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.49x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 310 ms: 1.41x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                   |
| async_tree_io              | 838 ms                                                 | 605 ms: 1.39x faster                                                   |
| async_tree_none            | 350 ms                                                 | 254 ms: 1.38x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 244 ms: 1.31x faster                                                   |
| async_generators           | 433 ms                                                 | 382 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 528 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 514 ms: 1.06x faster                                                   |
| coroutines                 | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.4 ms: 1.20x faster                                                  |
| nbody          | 87.7 ms                                                | 81.8 ms: 1.07x faster                                                  |
| pidigits       | 186 ms                                                 | 212 ms: 1.14x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.20 ms: 1.18x faster                                                  |
| regex_dna      | 220 ms                                                 | 197 ms: 1.12x faster                                                   |
| regex_compile  | 132 ms                                                 | 123 ms: 1.07x faster                                                   |
| regex_v8       | 26.9 ms                                                | 25.2 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|---------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads         | 2.12 sec                                               | 1.90 sec: 1.12x faster                                                 |
| xml_etree_process   | 60.5 ms                                                | 57.5 ms: 1.05x faster                                                  |
| xml_etree_generate  | 86.8 ms                                                | 84.6 ms: 1.03x faster                                                  |
| xml_etree_iterparse | 101 ms                                                 | 99.7 ms: 1.02x faster                                                  |
| xml_etree_parse     | 154 ms                                                 | 156 ms: 1.01x slower                                                   |
| json_loads          | 27.2 us                                                | 30.2 us: 1.11x slower                                                  |
| json_dumps          | 10.1 ms                                                | 12.2 ms: 1.21x slower                                                  |
| Geometric mean      | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.96 ms: 1.01x faster                                                  |
| python_startup         | 12.7 ms                                                | 12.6 ms: 1.00x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.5 ms: 1.10x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 47.6 ms: 1.06x faster                                                  |
| django_template | 31.7 ms                                                | 30.3 ms: 1.05x faster                                                  |
| mako            | 10.7 ms                                                | 11.5 ms: 1.07x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.49x faster                                                   |
| deepcopy                   | 354 us                                                 | 245 us: 1.45x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 310 ms: 1.41x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                   |
| async_tree_io              | 838 ms                                                 | 605 ms: 1.39x faster                                                   |
| async_tree_none            | 350 ms                                                 | 254 ms: 1.38x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 28.6 us: 1.34x faster                                                  |
| spectral_norm              | 113 ms                                                 | 84.5 ms: 1.34x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 244 ms: 1.31x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.56 us: 1.27x faster                                                  |
| scimark_fft                | 367 ms                                                 | 292 ms: 1.26x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.02 ms: 1.25x faster                                                  |
| go                         | 141 ms                                                 | 113 ms: 1.24x faster                                                   |
| float                      | 78.7 ms                                                | 65.4 ms: 1.20x faster                                                  |
| pathlib                    | 17.4 ms                                                | 14.6 ms: 1.19x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.20 ms: 1.18x faster                                                  |
| telco                      | 8.40 ms                                                | 7.21 ms: 1.16x faster                                                  |
| pylint                     | 312 ms                                                 | 269 ms: 1.16x faster                                                   |
| pyflate                    | 470 ms                                                 | 405 ms: 1.16x faster                                                   |
| richards                   | 47.5 ms                                                | 41.2 ms: 1.15x faster                                                  |
| async_generators           | 433 ms                                                 | 382 ms: 1.13x faster                                                   |
| richards_super             | 53.7 ms                                                | 47.6 ms: 1.13x faster                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 59.4 ms: 1.12x faster                                                  |
| regex_dna                  | 220 ms                                                 | 197 ms: 1.12x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.90 sec: 1.12x faster                                                 |
| scimark_sor                | 122 ms                                                 | 110 ms: 1.11x faster                                                   |
| logging_silent             | 101 ns                                                 | 91.1 ns: 1.11x faster                                                  |
| genshi_text                | 22.6 ms                                                | 20.5 ms: 1.10x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.28 sec: 1.10x faster                                                 |
| comprehensions             | 16.5 us                                                | 15.1 us: 1.09x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 68.5 ms: 1.09x faster                                                  |
| nqueens                    | 80.9 ms                                                | 74.3 ms: 1.09x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.67 us: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 528 ms: 1.09x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                                 |
| 2to3                       | 266 ms                                                 | 247 ms: 1.08x faster                                                   |
| thrift                     | 800 us                                                 | 742 us: 1.08x faster                                                   |
| sqlglot_parse              | 1.26 ms                                                | 1.18 ms: 1.07x faster                                                  |
| nbody                      | 87.7 ms                                                | 81.8 ms: 1.07x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 124 ms: 1.07x faster                                                   |
| typing_runtime_protocols   | 160 us                                                 | 150 us: 1.07x faster                                                   |
| regex_compile              | 132 ms                                                 | 123 ms: 1.07x faster                                                   |
| logging_format             | 6.23 us                                                | 5.84 us: 1.07x faster                                                  |
| chaos                      | 58.0 ms                                                | 54.4 ms: 1.07x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.30 us: 1.07x faster                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 15.9 ms: 1.07x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 25.2 ms: 1.06x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 47.6 ms: 1.06x faster                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.48 ms: 1.06x faster                                                  |
| sympy_str                  | 273 ms                                                 | 258 ms: 1.06x faster                                                   |
| sqlglot_normalize          | 108 ms                                                 | 102 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 514 ms: 1.06x faster                                                   |
| sympy_sum                  | 150 ms                                                 | 142 ms: 1.06x faster                                                   |
| sphinx                     | 1.03 sec                                               | 978 ms: 1.06x faster                                                   |
| deltablue                  | 3.19 ms                                                | 3.03 ms: 1.05x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 57.5 ms: 1.05x faster                                                  |
| html5lib                   | 63.4 ms                                                | 60.3 ms: 1.05x faster                                                  |
| sympy_expand               | 456 ms                                                 | 435 ms: 1.05x faster                                                   |
| sympy_integrate            | 19.8 ms                                                | 18.9 ms: 1.05x faster                                                  |
| django_template            | 31.7 ms                                                | 30.3 ms: 1.05x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                 |
| generators                 | 28.8 ms                                                | 27.6 ms: 1.04x faster                                                  |
| scimark_lu                 | 114 ms                                                 | 110 ms: 1.04x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 62.0 ms: 1.04x faster                                                  |
| coverage                   | 82.8 ms                                                | 79.6 ms: 1.04x faster                                                  |
| sqlglot_optimize           | 53.4 ms                                                | 51.5 ms: 1.04x faster                                                  |
| hexiom                     | 6.08 ms                                                | 5.91 ms: 1.03x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 84.6 ms: 1.03x faster                                                  |
| fannkuch                   | 394 ms                                                 | 386 ms: 1.02x faster                                                   |
| coroutines                 | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                  |
| raytrace                   | 262 ms                                                 | 257 ms: 1.02x faster                                                   |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.02x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 99.7 ms: 1.02x faster                                                  |
| docutils                   | 2.58 sec                                               | 2.56 sec: 1.01x faster                                                 |
| python_startup_no_site     | 7.00 ms                                                | 6.96 ms: 1.01x faster                                                  |
| python_startup             | 12.7 ms                                                | 12.6 ms: 1.00x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.91 ms: 1.00x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 732 ms: 1.01x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 826 us: 1.01x slower                                                   |
| xml_etree_parse            | 154 ms                                                 | 156 ms: 1.01x slower                                                   |
| json                       | 5.32 ms                                                | 5.39 ms: 1.01x slower                                                  |
| mdp                        | 2.54 sec                                               | 2.60 sec: 1.02x slower                                                 |
| create_gc_cycles           | 2.45 ms                                                | 2.52 ms: 1.03x slower                                                  |
| many_optionals             | 857 us                                                 | 918 us: 1.07x slower                                                   |
| mako                       | 10.7 ms                                                | 11.5 ms: 1.07x slower                                                  |
| json_loads                 | 27.2 us                                                | 30.2 us: 1.11x slower                                                  |
| pidigits                   | 186 ms                                                 | 212 ms: 1.14x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 12.2 ms: 1.21x slower                                                  |
| subparsers                 | 15.5 ms                                                | 19.9 ms: 1.29x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 79.7 ms: 3.32x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (5): shortest_path, pickle_pure_python, unpickle_pure_python, asyncio_websockets, connected_components
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.080x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.03x