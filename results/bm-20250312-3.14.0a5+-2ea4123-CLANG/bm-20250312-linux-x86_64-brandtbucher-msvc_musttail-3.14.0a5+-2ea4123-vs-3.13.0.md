# Results vs. 3.13.0

- fork: brandtbucher
- ref: msvc_musttail
- machine: linux-x86_64
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.073x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 251 ms: 1.06x faster                                                  |
| docutils       | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                |
| html5lib       | 63.4 ms                                                | 57.3 ms: 1.11x faster                                                 |
| sphinx         | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 307 ms: 1.51x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 306 ms: 1.43x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 606 ms: 1.42x faster                                                  |
| async_tree_none            | 350 ms                                                 | 249 ms: 1.41x faster                                                  |
| async_tree_io              | 838 ms                                                 | 596 ms: 1.41x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 242 ms: 1.32x faster                                                  |
| async_generators           | 433 ms                                                 | 368 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 517 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 504 ms: 1.08x faster                                                  |
| coroutines                 | 22.2 ms                                                | 22.1 ms: 1.01x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.8 ms: 1.18x faster                                                 |
| nbody          | 87.7 ms                                                | 86.4 ms: 1.01x faster                                                 |
| pidigits       | 186 ms                                                 | 219 ms: 1.18x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.28 ms: 1.15x faster                                                 |
| regex_v8       | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                 |
| regex_dna      | 220 ms                                                 | 196 ms: 1.12x faster                                                  |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.88 sec: 1.13x faster                                                |
| xml_etree_process    | 60.5 ms                                                | 58.7 ms: 1.03x faster                                                 |
| pickle_pure_python   | 302 us                                                 | 306 us: 1.01x slower                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 103 ms: 1.02x slower                                                  |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                  |
| xml_etree_parse      | 154 ms                                                 | 163 ms: 1.06x slower                                                  |
| json_loads           | 27.2 us                                                | 28.9 us: 1.06x slower                                                 |
| json_dumps           | 10.1 ms                                                | 12.5 ms: 1.23x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                 |
| python_startup         | 12.7 ms                                                | 12.7 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                 |
| genshi_xml      | 50.5 ms                                                | 48.1 ms: 1.05x faster                                                 |
| django_template | 31.7 ms                                                | 30.6 ms: 1.04x faster                                                 |
| mako            | 10.7 ms                                                | 11.6 ms: 1.09x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 307 ms: 1.51x faster                                                  |
| deepcopy                   | 354 us                                                 | 244 us: 1.45x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 306 ms: 1.43x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 606 ms: 1.42x faster                                                  |
| async_tree_none            | 350 ms                                                 | 249 ms: 1.41x faster                                                  |
| async_tree_io              | 838 ms                                                 | 596 ms: 1.41x faster                                                  |
| spectral_norm              | 113 ms                                                 | 82.5 ms: 1.37x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 242 ms: 1.32x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.4 us: 1.31x faster                                                 |
| deepcopy_reduce            | 3.24 us                                                | 2.53 us: 1.28x faster                                                 |
| scimark_fft                | 367 ms                                                 | 289 ms: 1.27x faster                                                  |
| go                         | 141 ms                                                 | 113 ms: 1.25x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.14 ms: 1.21x faster                                                 |
| async_generators           | 433 ms                                                 | 368 ms: 1.18x faster                                                  |
| float                      | 78.7 ms                                                | 66.8 ms: 1.18x faster                                                 |
| pathlib                    | 17.4 ms                                                | 14.9 ms: 1.17x faster                                                 |
| logging_silent             | 101 ns                                                 | 87.1 ns: 1.16x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.28 ms: 1.15x faster                                                 |
| scimark_sor                | 122 ms                                                 | 107 ms: 1.15x faster                                                  |
| pyflate                    | 470 ms                                                 | 410 ms: 1.15x faster                                                  |
| telco                      | 8.40 ms                                                | 7.39 ms: 1.14x faster                                                 |
| pylint                     | 312 ms                                                 | 275 ms: 1.13x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                 |
| tomli_loads                | 2.12 sec                                               | 1.88 sec: 1.13x faster                                                |
| regex_dna                  | 220 ms                                                 | 196 ms: 1.12x faster                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 60.1 ms: 1.11x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 517 ms: 1.11x faster                                                  |
| html5lib                   | 63.4 ms                                                | 57.3 ms: 1.11x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.66 us: 1.09x faster                                                 |
| chaos                      | 58.0 ms                                                | 53.3 ms: 1.09x faster                                                 |
| thrift                     | 800 us                                                 | 737 us: 1.09x faster                                                  |
| typing_runtime_protocols   | 160 us                                                 | 148 us: 1.09x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 504 ms: 1.08x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.26 us: 1.07x faster                                                 |
| nqueens                    | 80.9 ms                                                | 75.4 ms: 1.07x faster                                                 |
| scimark_lu                 | 114 ms                                                 | 107 ms: 1.07x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.39 sec: 1.07x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                 |
| logging_format             | 6.23 us                                                | 5.86 us: 1.06x faster                                                 |
| comprehensions             | 16.5 us                                                | 15.5 us: 1.06x faster                                                 |
| deltablue                  | 3.19 ms                                                | 3.01 ms: 1.06x faster                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 126 ms: 1.06x faster                                                  |
| hexiom                     | 6.08 ms                                                | 5.74 ms: 1.06x faster                                                 |
| 2to3                       | 266 ms                                                 | 251 ms: 1.06x faster                                                  |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                                  |
| sympy_str                  | 273 ms                                                 | 258 ms: 1.06x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 143 ms: 1.06x faster                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.1 ms: 1.05x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 48.1 ms: 1.05x faster                                                 |
| sympy_integrate            | 19.8 ms                                                | 18.9 ms: 1.05x faster                                                 |
| dulwich_log                | 64.6 ms                                                | 61.8 ms: 1.04x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                |
| coverage                   | 82.8 ms                                                | 79.6 ms: 1.04x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                |
| sympy_expand               | 456 ms                                                 | 440 ms: 1.04x faster                                                  |
| django_template            | 31.7 ms                                                | 30.6 ms: 1.04x faster                                                 |
| crypto_pyaes               | 74.7 ms                                                | 72.5 ms: 1.03x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 58.7 ms: 1.03x faster                                                 |
| sphinx                     | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                |
| raytrace                   | 262 ms                                                 | 255 ms: 1.03x faster                                                  |
| shortest_path              | 487 ms                                                 | 480 ms: 1.01x faster                                                  |
| nbody                      | 87.7 ms                                                | 86.4 ms: 1.01x faster                                                 |
| coroutines                 | 22.2 ms                                                | 22.1 ms: 1.01x faster                                                 |
| generators                 | 28.8 ms                                                | 28.6 ms: 1.01x faster                                                 |
| richards                   | 47.5 ms                                                | 47.4 ms: 1.00x faster                                                 |
| python_startup_no_site     | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                 |
| python_startup             | 12.7 ms                                                | 12.7 ms: 1.00x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                |
| pprint_safe_repr           | 727 ms                                                 | 736 ms: 1.01x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 306 us: 1.01x slower                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 103 ms: 1.02x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 4.97 ms: 1.02x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 831 us: 1.02x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.51 sec: 1.02x slower                                                |
| meteor_contest             | 108 ms                                                 | 111 ms: 1.02x slower                                                  |
| richards_super             | 53.7 ms                                                | 55.6 ms: 1.04x slower                                                 |
| create_gc_cycles           | 2.45 ms                                                | 2.54 ms: 1.04x slower                                                 |
| mdp                        | 2.54 sec                                               | 2.65 sec: 1.04x slower                                                |
| xml_etree_parse            | 154 ms                                                 | 163 ms: 1.06x slower                                                  |
| json_loads                 | 27.2 us                                                | 28.9 us: 1.06x slower                                                 |
| many_optionals             | 857 us                                                 | 924 us: 1.08x slower                                                  |
| mako                       | 10.7 ms                                                | 11.6 ms: 1.09x slower                                                 |
| pidigits                   | 186 ms                                                 | 219 ms: 1.18x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 12.5 ms: 1.23x slower                                                 |
| subparsers                 | 15.5 ms                                                | 20.2 ms: 1.31x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 80.9 ms: 3.37x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (5): json, connected_components, fannkuch, asyncio_websockets, xml_etree_generate
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250312-3.14.0a5+-2ea4123-CLANG/bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.073x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.03x