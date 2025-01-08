# Results vs. base

- fork: Fidget-Spinner
- ref: tail_call
- machine: linux-x86_64
- commit hash: f1d3190
- commit date: 2025-01-07
- overall geometric mean: 1.074x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 249 ms: 1.06x faster                                                  |
| docutils       | 2.63 sec                                                               | 2.58 sec: 1.02x faster                                                |
| html5lib       | 64.5 ms                                                                | 57.9 ms: 1.12x faster                                                 |
| sphinx         | 1.03 sec                                                               | 991 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.06x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                 | 23.7 ms                                                                | 21.2 ms: 1.12x faster                                                 |
| async_tree_memoization     | 339 ms                                                                 | 313 ms: 1.08x faster                                                  |
| async_tree_memoization_tg  | 313 ms                                                                 | 290 ms: 1.08x faster                                                  |
| async_tree_none            | 275 ms                                                                 | 256 ms: 1.08x faster                                                  |
| async_tree_none_tg         | 253 ms                                                                 | 236 ms: 1.07x faster                                                  |
| async_tree_io_tg           | 612 ms                                                                 | 573 ms: 1.07x faster                                                  |
| async_tree_io              | 636 ms                                                                 | 597 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed    | 504 ms                                                                 | 482 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                 | 467 ms: 1.04x faster                                                  |
| async_generators           | 434 ms                                                                 | 427 ms: 1.02x faster                                                  |
| Geometric mean             | (ref)                                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 98.0 ms                                                                | 83.6 ms: 1.17x faster                                                 |
| float          | 73.4 ms                                                                | 66.4 ms: 1.11x faster                                                 |
| pidigits       | 197 ms                                                                 | 197 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 139 ms                                                                 | 125 ms: 1.11x faster                                                  |
| regex_v8       | 24.2 ms                                                                | 24.8 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                                               | 1.89 sec: 1.14x faster                                                |
| pickle_pure_python   | 337 us                                                                 | 302 us: 1.11x faster                                                  |
| unpickle_pure_python | 232 us                                                                 | 210 us: 1.10x faster                                                  |
| xml_etree_process    | 63.6 ms                                                                | 57.8 ms: 1.10x faster                                                 |
| xml_etree_generate   | 90.5 ms                                                                | 85.2 ms: 1.06x faster                                                 |
| json_dumps           | 12.6 ms                                                                | 12.1 ms: 1.04x faster                                                 |
| xml_etree_iterparse  | 104 ms                                                                 | 101 ms: 1.03x faster                                                  |
| json_loads           | 27.4 us                                                                | 26.6 us: 1.03x faster                                                 |
| xml_etree_parse      | 163 ms                                                                 | 162 ms: 1.01x faster                                                  |
| Geometric mean       | (ref)                                                                  | 1.07x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                                 |
| python_startup_no_site | 7.04 ms                                                                | 6.98 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 55.9 ms                                                                | 48.0 ms: 1.16x faster                                                 |
| genshi_text     | 24.0 ms                                                                | 21.3 ms: 1.13x faster                                                 |
| mako            | 12.6 ms                                                                | 11.2 ms: 1.12x faster                                                 |
| django_template | 34.4 ms                                                                | 30.7 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                                  | 1.13x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| scimark_sor                | 135 ms                                                                 | 109 ms: 1.24x faster                                                  |
| deltablue                  | 3.65 ms                                                                | 2.98 ms: 1.23x faster                                                 |
| logging_format             | 7.24 us                                                                | 6.03 us: 1.20x faster                                                 |
| logging_simple             | 6.43 us                                                                | 5.43 us: 1.18x faster                                                 |
| go                         | 127 ms                                                                 | 109 ms: 1.17x faster                                                  |
| nbody                      | 98.0 ms                                                                | 83.6 ms: 1.17x faster                                                 |
| genshi_xml                 | 55.9 ms                                                                | 48.0 ms: 1.16x faster                                                 |
| hexiom                     | 6.74 ms                                                                | 5.80 ms: 1.16x faster                                                 |
| logging_silent             | 107 ns                                                                 | 93.0 ns: 1.15x faster                                                 |
| richards                   | 46.4 ms                                                                | 40.4 ms: 1.15x faster                                                 |
| chaos                      | 62.3 ms                                                                | 54.2 ms: 1.15x faster                                                 |
| tomli_loads                | 2.14 sec                                                               | 1.89 sec: 1.14x faster                                                |
| genshi_text                | 24.0 ms                                                                | 21.3 ms: 1.13x faster                                                 |
| nqueens                    | 83.4 ms                                                                | 74.1 ms: 1.13x faster                                                 |
| coroutines                 | 23.7 ms                                                                | 21.2 ms: 1.12x faster                                                 |
| mako                       | 12.6 ms                                                                | 11.2 ms: 1.12x faster                                                 |
| django_template            | 34.4 ms                                                                | 30.7 ms: 1.12x faster                                                 |
| scimark_lu                 | 113 ms                                                                 | 101 ms: 1.12x faster                                                  |
| html5lib                   | 64.5 ms                                                                | 57.9 ms: 1.12x faster                                                 |
| pickle_pure_python         | 337 us                                                                 | 302 us: 1.11x faster                                                  |
| scimark_monte_carlo        | 64.8 ms                                                                | 58.3 ms: 1.11x faster                                                 |
| comprehensions             | 17.9 us                                                                | 16.1 us: 1.11x faster                                                 |
| pyflate                    | 451 ms                                                                 | 407 ms: 1.11x faster                                                  |
| regex_compile              | 139 ms                                                                 | 125 ms: 1.11x faster                                                  |
| sqlglot_parse              | 1.31 ms                                                                | 1.19 ms: 1.11x faster                                                 |
| float                      | 73.4 ms                                                                | 66.4 ms: 1.11x faster                                                 |
| deepcopy_memo              | 32.1 us                                                                | 29.0 us: 1.11x faster                                                 |
| unpickle_pure_python       | 232 us                                                                 | 210 us: 1.10x faster                                                  |
| pprint_pformat             | 1.66 sec                                                               | 1.51 sec: 1.10x faster                                                |
| subparsers                 | 22.6 ms                                                                | 20.5 ms: 1.10x faster                                                 |
| generators                 | 29.9 ms                                                                | 27.1 ms: 1.10x faster                                                 |
| deepcopy                   | 275 us                                                                 | 250 us: 1.10x faster                                                  |
| richards_super             | 51.9 ms                                                                | 47.1 ms: 1.10x faster                                                 |
| xml_etree_process          | 63.6 ms                                                                | 57.8 ms: 1.10x faster                                                 |
| sqlglot_transpile          | 1.64 ms                                                                | 1.50 ms: 1.10x faster                                                 |
| raytrace                   | 277 ms                                                                 | 252 ms: 1.10x faster                                                  |
| pprint_safe_repr           | 813 ms                                                                 | 746 ms: 1.09x faster                                                  |
| spectral_norm              | 98.8 ms                                                                | 90.8 ms: 1.09x faster                                                 |
| crypto_pyaes               | 75.2 ms                                                                | 69.4 ms: 1.08x faster                                                 |
| scimark_fft                | 326 ms                                                                 | 301 ms: 1.08x faster                                                  |
| async_tree_memoization     | 339 ms                                                                 | 313 ms: 1.08x faster                                                  |
| fannkuch                   | 417 ms                                                                 | 386 ms: 1.08x faster                                                  |
| sqlglot_normalize          | 111 ms                                                                 | 103 ms: 1.08x faster                                                  |
| async_tree_memoization_tg  | 313 ms                                                                 | 290 ms: 1.08x faster                                                  |
| async_tree_none            | 275 ms                                                                 | 256 ms: 1.08x faster                                                  |
| async_tree_none_tg         | 253 ms                                                                 | 236 ms: 1.07x faster                                                  |
| deepcopy_reduce            | 2.78 us                                                                | 2.60 us: 1.07x faster                                                 |
| async_tree_io_tg           | 612 ms                                                                 | 573 ms: 1.07x faster                                                  |
| pycparser                  | 1.19 sec                                                               | 1.11 sec: 1.07x faster                                                |
| sqlglot_optimize           | 55.9 ms                                                                | 52.4 ms: 1.07x faster                                                 |
| async_tree_io              | 636 ms                                                                 | 597 ms: 1.06x faster                                                  |
| dulwich_log                | 66.4 ms                                                                | 62.4 ms: 1.06x faster                                                 |
| typing_runtime_protocols   | 164 us                                                                 | 154 us: 1.06x faster                                                  |
| xml_etree_generate         | 90.5 ms                                                                | 85.2 ms: 1.06x faster                                                 |
| sympy_expand               | 472 ms                                                                 | 444 ms: 1.06x faster                                                  |
| sqlalchemy_imperative      | 17.4 ms                                                                | 16.4 ms: 1.06x faster                                                 |
| sympy_str                  | 277 ms                                                                 | 261 ms: 1.06x faster                                                  |
| many_optionals             | 992 us                                                                 | 937 us: 1.06x faster                                                  |
| bpe_tokeniser              | 4.67 sec                                                               | 4.42 sec: 1.06x faster                                                |
| 2to3                       | 263 ms                                                                 | 249 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult    | 4.31 ms                                                                | 4.09 ms: 1.05x faster                                                 |
| sqlalchemy_declarative     | 134 ms                                                                 | 127 ms: 1.05x faster                                                  |
| bench_thread_pool          | 872 us                                                                 | 829 us: 1.05x faster                                                  |
| sympy_sum                  | 151 ms                                                                 | 144 ms: 1.05x faster                                                  |
| thrift                     | 799 us                                                                 | 762 us: 1.05x faster                                                  |
| sympy_integrate            | 20.0 ms                                                                | 19.1 ms: 1.05x faster                                                 |
| async_tree_cpu_io_mixed    | 504 ms                                                                 | 482 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                 | 467 ms: 1.04x faster                                                  |
| json_dumps                 | 12.6 ms                                                                | 12.1 ms: 1.04x faster                                                 |
| telco                      | 7.57 ms                                                                | 7.29 ms: 1.04x faster                                                 |
| sphinx                     | 1.03 sec                                                               | 991 ms: 1.04x faster                                                  |
| pylint                     | 283 ms                                                                 | 273 ms: 1.04x faster                                                  |
| meteor_contest             | 115 ms                                                                 | 111 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 104 ms                                                                 | 101 ms: 1.03x faster                                                  |
| json                       | 5.06 ms                                                                | 4.91 ms: 1.03x faster                                                 |
| json_loads                 | 27.4 us                                                                | 26.6 us: 1.03x faster                                                 |
| pathlib                    | 14.5 ms                                                                | 14.2 ms: 1.02x faster                                                 |
| docutils                   | 2.63 sec                                                               | 2.58 sec: 1.02x faster                                                |
| gc_traversal               | 5.05 ms                                                                | 4.96 ms: 1.02x faster                                                 |
| async_generators           | 434 ms                                                                 | 427 ms: 1.02x faster                                                  |
| bench_mp_pool              | 81.7 ms                                                                | 80.7 ms: 1.01x faster                                                 |
| sqlite_synth               | 2.76 us                                                                | 2.72 us: 1.01x faster                                                 |
| mdp                        | 2.92 sec                                                               | 2.88 sec: 1.01x faster                                                |
| python_startup             | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                                 |
| xml_etree_parse            | 163 ms                                                                 | 162 ms: 1.01x faster                                                  |
| python_startup_no_site     | 7.04 ms                                                                | 6.98 ms: 1.01x faster                                                 |
| shortest_path              | 480 ms                                                                 | 477 ms: 1.01x faster                                                  |
| pidigits                   | 197 ms                                                                 | 197 ms: 1.00x faster                                                  |
| create_gc_cycles           | 2.51 ms                                                                | 2.54 ms: 1.01x slower                                                 |
| regex_v8                   | 24.2 ms                                                                | 24.8 ms: 1.03x slower                                                 |
| Geometric mean             | (ref)                                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (6): coverage, regex_effbot, connected_components, regex_dna, asyncio_websockets, k_core

- Geometric mean (including insignificant results): 1.074x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.00x