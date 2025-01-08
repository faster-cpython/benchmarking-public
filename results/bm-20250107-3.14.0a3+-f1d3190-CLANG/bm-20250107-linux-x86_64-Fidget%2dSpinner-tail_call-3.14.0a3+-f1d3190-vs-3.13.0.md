# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: tail_call
- machine: linux-x86_64
- commit hash: f1d3190
- commit date: 2025-01-07
- overall geometric mean: 1.080x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 249 ms: 1.07x faster                                                  |
| html5lib       | 63.4 ms                                                | 57.9 ms: 1.10x faster                                                 |
| sphinx         | 1.03 sec                                               | 991 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 290 ms: 1.60x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 573 ms: 1.50x faster                                                  |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                                  |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 236 ms: 1.36x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 482 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 467 ms: 1.16x faster                                                  |
| coroutines                 | 22.2 ms                                                | 21.2 ms: 1.05x faster                                                 |
| async_generators           | 433 ms                                                 | 427 ms: 1.01x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.26x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.4 ms: 1.19x faster                                                 |
| nbody          | 87.7 ms                                                | 83.6 ms: 1.05x faster                                                 |
| pidigits       | 186 ms                                                 | 197 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.18 ms: 1.18x faster                                                 |
| regex_dna      | 220 ms                                                 | 196 ms: 1.12x faster                                                  |
| regex_v8       | 26.9 ms                                                | 24.8 ms: 1.08x faster                                                 |
| regex_compile  | 132 ms                                                 | 125 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.89 sec: 1.12x faster                                                |
| xml_etree_process    | 60.5 ms                                                | 57.8 ms: 1.05x faster                                                 |
| json_loads           | 27.2 us                                                | 26.6 us: 1.02x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 85.2 ms: 1.02x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 210 us: 1.01x faster                                                  |
| xml_etree_parse      | 154 ms                                                 | 162 ms: 1.05x slower                                                  |
| json_dumps           | 10.1 ms                                                | 12.1 ms: 1.20x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.98 ms: 1.00x faster                                                 |
| python_startup         | 12.7 ms                                                | 12.7 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                 |
| genshi_xml      | 50.5 ms                                                | 48.0 ms: 1.05x faster                                                 |
| django_template | 31.7 ms                                                | 30.7 ms: 1.03x faster                                                 |
| mako            | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 290 ms: 1.60x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 573 ms: 1.50x faster                                                  |
| deepcopy                   | 354 us                                                 | 250 us: 1.42x faster                                                  |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                                  |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 236 ms: 1.36x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.0 us: 1.32x faster                                                 |
| go                         | 141 ms                                                 | 109 ms: 1.29x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.60 us: 1.25x faster                                                 |
| spectral_norm              | 113 ms                                                 | 90.8 ms: 1.25x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.09 ms: 1.23x faster                                                 |
| pathlib                    | 17.4 ms                                                | 14.2 ms: 1.23x faster                                                 |
| scimark_fft                | 367 ms                                                 | 301 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 482 ms: 1.19x faster                                                  |
| float                      | 78.7 ms                                                | 66.4 ms: 1.19x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.18 ms: 1.18x faster                                                 |
| richards                   | 47.5 ms                                                | 40.4 ms: 1.18x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 467 ms: 1.16x faster                                                  |
| pyflate                    | 470 ms                                                 | 407 ms: 1.15x faster                                                  |
| telco                      | 8.40 ms                                                | 7.29 ms: 1.15x faster                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 58.3 ms: 1.15x faster                                                 |
| pylint                     | 312 ms                                                 | 273 ms: 1.14x faster                                                  |
| richards_super             | 53.7 ms                                                | 47.1 ms: 1.14x faster                                                 |
| scimark_lu                 | 114 ms                                                 | 101 ms: 1.13x faster                                                  |
| scimark_sor                | 122 ms                                                 | 109 ms: 1.12x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.89 sec: 1.12x faster                                                |
| regex_dna                  | 220 ms                                                 | 196 ms: 1.12x faster                                                  |
| html5lib                   | 63.4 ms                                                | 57.9 ms: 1.10x faster                                                 |
| nqueens                    | 80.9 ms                                                | 74.1 ms: 1.09x faster                                                 |
| logging_silent             | 101 ns                                                 | 93.0 ns: 1.09x faster                                                 |
| json                       | 5.32 ms                                                | 4.91 ms: 1.08x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 24.8 ms: 1.08x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                                |
| crypto_pyaes               | 74.7 ms                                                | 69.4 ms: 1.08x faster                                                 |
| deltablue                  | 3.19 ms                                                | 2.98 ms: 1.07x faster                                                 |
| chaos                      | 58.0 ms                                                | 54.2 ms: 1.07x faster                                                 |
| 2to3                       | 266 ms                                                 | 249 ms: 1.07x faster                                                  |
| sqlglot_parse              | 1.26 ms                                                | 1.19 ms: 1.07x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.72 us: 1.07x faster                                                 |
| genshi_text                | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.42 sec: 1.06x faster                                                |
| generators                 | 28.8 ms                                                | 27.1 ms: 1.06x faster                                                 |
| regex_compile              | 132 ms                                                 | 125 ms: 1.05x faster                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.50 ms: 1.05x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 48.0 ms: 1.05x faster                                                 |
| sqlglot_normalize          | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| thrift                     | 800 us                                                 | 762 us: 1.05x faster                                                  |
| coroutines                 | 22.2 ms                                                | 21.2 ms: 1.05x faster                                                 |
| nbody                      | 87.7 ms                                                | 83.6 ms: 1.05x faster                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.05x faster                                                  |
| hexiom                     | 6.08 ms                                                | 5.80 ms: 1.05x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 57.8 ms: 1.05x faster                                                 |
| sympy_str                  | 273 ms                                                 | 261 ms: 1.04x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 144 ms: 1.04x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                |
| logging_simple             | 5.65 us                                                | 5.43 us: 1.04x faster                                                 |
| sphinx                     | 1.03 sec                                               | 991 ms: 1.04x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.1 ms: 1.04x faster                                                 |
| typing_runtime_protocols   | 160 us                                                 | 154 us: 1.04x faster                                                  |
| raytrace                   | 262 ms                                                 | 252 ms: 1.04x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 62.4 ms: 1.04x faster                                                 |
| logging_format             | 6.23 us                                                | 6.03 us: 1.03x faster                                                 |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                                 |
| django_template            | 31.7 ms                                                | 30.7 ms: 1.03x faster                                                 |
| sympy_expand               | 456 ms                                                 | 444 ms: 1.03x faster                                                  |
| comprehensions             | 16.5 us                                                | 16.1 us: 1.02x faster                                                 |
| coverage                   | 82.8 ms                                                | 81.1 ms: 1.02x faster                                                 |
| json_loads                 | 27.2 us                                                | 26.6 us: 1.02x faster                                                 |
| fannkuch                   | 394 ms                                                 | 386 ms: 1.02x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 85.2 ms: 1.02x faster                                                 |
| shortest_path              | 487 ms                                                 | 477 ms: 1.02x faster                                                  |
| sqlglot_optimize           | 53.4 ms                                                | 52.4 ms: 1.02x faster                                                 |
| async_generators           | 433 ms                                                 | 427 ms: 1.01x faster                                                  |
| unpickle_pure_python       | 213 us                                                 | 210 us: 1.01x faster                                                  |
| connected_components       | 447 ms                                                 | 443 ms: 1.01x faster                                                  |
| python_startup_no_site     | 7.00 ms                                                | 6.98 ms: 1.00x faster                                                 |
| python_startup             | 12.7 ms                                                | 12.7 ms: 1.00x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 829 us: 1.01x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 4.96 ms: 1.01x slower                                                 |
| pprint_pformat             | 1.48 sec                                               | 1.51 sec: 1.02x slower                                                |
| meteor_contest             | 108 ms                                                 | 111 ms: 1.03x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 746 ms: 1.03x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.54 ms: 1.04x slower                                                 |
| xml_etree_parse            | 154 ms                                                 | 162 ms: 1.05x slower                                                  |
| mako                       | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                 |
| pidigits                   | 186 ms                                                 | 197 ms: 1.06x slower                                                  |
| many_optionals             | 857 us                                                 | 937 us: 1.09x slower                                                  |
| mdp                        | 2.54 sec                                               | 2.88 sec: 1.13x slower                                                |
| json_dumps                 | 10.1 ms                                                | 12.1 ms: 1.20x slower                                                 |
| subparsers                 | 15.5 ms                                                | 20.5 ms: 1.32x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 80.7 ms: 3.36x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (4): xml_etree_iterparse, docutils, asyncio_websockets, pickle_pure_python
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.080x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.03x