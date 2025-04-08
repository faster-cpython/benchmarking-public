# Results vs. 3.13.0

- fork: brandtbucher
- ref: non_methods
- machine: linux-x86_64
- commit hash: fe5b174
- commit date: 2025-04-07
- overall geometric mean: 1.068x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 250 ms: 1.06x faster                                                |
| docutils       | 2.58 sec                                               | 2.59 sec: 1.00x slower                                              |
| html5lib       | 63.4 ms                                                | 61.2 ms: 1.04x faster                                               |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 308 ms: 1.42x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 608 ms: 1.42x faster                                                |
| async_tree_io              | 838 ms                                                 | 609 ms: 1.38x faster                                                |
| async_tree_none            | 350 ms                                                 | 255 ms: 1.38x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 245 ms: 1.30x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 483 ms: 1.19x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                |
| async_generators           | 433 ms                                                 | 389 ms: 1.11x faster                                                |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.05x slower                                               |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.8 ms: 1.20x faster                                               |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                |
| nbody          | 87.7 ms                                                | 90.9 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.19 ms: 1.18x faster                                               |
| regex_v8       | 26.9 ms                                                | 24.1 ms: 1.11x faster                                               |
| regex_compile  | 132 ms                                                 | 123 ms: 1.07x faster                                                |
| regex_dna      | 220 ms                                                 | 214 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads         | 2.12 sec                                               | 1.89 sec: 1.12x faster                                              |
| xml_etree_parse     | 154 ms                                                 | 141 ms: 1.09x faster                                                |
| xml_etree_generate  | 86.8 ms                                                | 83.2 ms: 1.04x faster                                               |
| xml_etree_process   | 60.5 ms                                                | 58.0 ms: 1.04x faster                                               |
| xml_etree_iterparse | 101 ms                                                 | 98.7 ms: 1.03x faster                                               |
| pickle_pure_python  | 302 us                                                 | 310 us: 1.03x slower                                                |
| json_loads          | 27.2 us                                                | 29.8 us: 1.10x slower                                               |
| json_dumps          | 10.1 ms                                                | 11.7 ms: 1.15x slower                                               |
| Geometric mean      | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                               |
| python_startup_no_site | 7.00 ms                                                | 8.21 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 20.9 ms: 1.08x faster                                               |
| genshi_xml     | 50.5 ms                                                | 48.6 ms: 1.04x faster                                               |
| mako           | 10.7 ms                                                | 11.0 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.06x faster                                              |
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                                |
| deepcopy                   | 354 us                                                 | 246 us: 1.44x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 308 ms: 1.42x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 608 ms: 1.42x faster                                                |
| async_tree_io              | 838 ms                                                 | 609 ms: 1.38x faster                                                |
| async_tree_none            | 350 ms                                                 | 255 ms: 1.38x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 28.4 us: 1.35x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 245 ms: 1.30x faster                                                |
| go                         | 141 ms                                                 | 109 ms: 1.28x faster                                                |
| deepcopy_reduce            | 3.24 us                                                | 2.60 us: 1.25x faster                                               |
| float                      | 78.7 ms                                                | 65.8 ms: 1.20x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 483 ms: 1.19x faster                                                |
| regex_effbot               | 3.77 ms                                                | 3.19 ms: 1.18x faster                                               |
| spectral_norm              | 113 ms                                                 | 97.7 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                                |
| richards                   | 47.5 ms                                                | 42.2 ms: 1.13x faster                                               |
| richards_super             | 53.7 ms                                                | 47.8 ms: 1.13x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.89 sec: 1.12x faster                                              |
| async_generators           | 433 ms                                                 | 389 ms: 1.11x faster                                                |
| regex_v8                   | 26.9 ms                                                | 24.1 ms: 1.11x faster                                               |
| telco                      | 8.40 ms                                                | 7.65 ms: 1.10x faster                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.60 ms: 1.09x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                |
| scimark_fft                | 367 ms                                                 | 336 ms: 1.09x faster                                                |
| dulwich_log                | 64.6 ms                                                | 59.4 ms: 1.09x faster                                               |
| genshi_text                | 22.6 ms                                                | 20.9 ms: 1.08x faster                                               |
| logging_silent             | 101 ns                                                 | 93.5 ns: 1.08x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.08x faster                                              |
| regex_compile              | 132 ms                                                 | 123 ms: 1.07x faster                                                |
| 2to3                       | 266 ms                                                 | 250 ms: 1.06x faster                                                |
| pyflate                    | 470 ms                                                 | 443 ms: 1.06x faster                                                |
| scimark_sor                | 122 ms                                                 | 115 ms: 1.06x faster                                                |
| gc_traversal               | 4.90 ms                                                | 4.64 ms: 1.05x faster                                               |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.05x faster                                               |
| chaos                      | 58.0 ms                                                | 55.3 ms: 1.05x faster                                               |
| bpe_tokeniser              | 4.69 sec                                               | 4.49 sec: 1.05x faster                                              |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.05x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 83.2 ms: 1.04x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 58.0 ms: 1.04x faster                                               |
| scimark_monte_carlo        | 66.8 ms                                                | 64.1 ms: 1.04x faster                                               |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                               |
| genshi_xml                 | 50.5 ms                                                | 48.6 ms: 1.04x faster                                               |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                              |
| html5lib                   | 63.4 ms                                                | 61.2 ms: 1.04x faster                                               |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                |
| crypto_pyaes               | 74.7 ms                                                | 72.3 ms: 1.03x faster                                               |
| regex_dna                  | 220 ms                                                 | 214 ms: 1.03x faster                                                |
| logging_format             | 6.23 us                                                | 6.07 us: 1.03x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 98.7 ms: 1.03x faster                                               |
| logging_simple             | 5.65 us                                                | 5.53 us: 1.02x faster                                               |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                              |
| raytrace                   | 262 ms                                                 | 256 ms: 1.02x faster                                                |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                |
| pprint_pformat             | 1.48 sec                                               | 1.45 sec: 1.02x faster                                              |
| pprint_safe_repr           | 727 ms                                                 | 715 ms: 1.02x faster                                                |
| nqueens                    | 80.9 ms                                                | 79.8 ms: 1.01x faster                                               |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                                |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                               |
| scimark_lu                 | 114 ms                                                 | 113 ms: 1.01x faster                                                |
| sympy_expand               | 456 ms                                                 | 453 ms: 1.01x faster                                                |
| comprehensions             | 16.5 us                                                | 16.4 us: 1.00x faster                                               |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                |
| docutils                   | 2.58 sec                                               | 2.59 sec: 1.00x slower                                              |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                               |
| shortest_path              | 487 ms                                                 | 494 ms: 1.02x slower                                                |
| typing_runtime_protocols   | 160 us                                                 | 163 us: 1.02x slower                                                |
| hexiom                     | 6.08 ms                                                | 6.18 ms: 1.02x slower                                               |
| connected_components       | 447 ms                                                 | 457 ms: 1.02x slower                                                |
| deltablue                  | 3.19 ms                                                | 3.27 ms: 1.02x slower                                               |
| pickle_pure_python         | 302 us                                                 | 310 us: 1.03x slower                                                |
| coverage                   | 82.8 ms                                                | 85.1 ms: 1.03x slower                                               |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                               |
| fannkuch                   | 394 ms                                                 | 407 ms: 1.03x slower                                                |
| nbody                      | 87.7 ms                                                | 90.9 ms: 1.04x slower                                               |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                               |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.05x slower                                               |
| generators                 | 28.8 ms                                                | 30.1 ms: 1.05x slower                                               |
| bench_thread_pool          | 818 us                                                 | 877 us: 1.07x slower                                                |
| many_optionals             | 857 us                                                 | 924 us: 1.08x slower                                                |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                               |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.15x slower                                               |
| python_startup_no_site     | 7.00 ms                                                | 8.21 ms: 1.17x slower                                               |
| subparsers                 | 15.5 ms                                                | 20.5 ms: 1.33x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 82.0 ms: 3.42x slower                                               |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                        |

Benchmark hidden because not significant (4): django_template, unpickle_pure_python, asyncio_websockets, json
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250407-3.14.0a6+-fe5b174/bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.068x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.03x