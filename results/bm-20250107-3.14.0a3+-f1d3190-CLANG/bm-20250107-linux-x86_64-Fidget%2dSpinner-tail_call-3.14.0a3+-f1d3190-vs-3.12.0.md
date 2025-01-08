# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: tail_call
- machine: linux-x86_64
- commit hash: f1d3190
- commit date: 2025-01-07
- overall geometric mean: 1.154x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 249 ms: 1.10x faster                                                  |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 573 ms: 2.06x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 290 ms: 1.98x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 597 ms: 1.94x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 236 ms: 1.91x faster                                                  |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 467 ms: 1.55x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 482 ms: 1.51x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.82x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 66.4 ms: 1.28x faster                                                 |
| nbody          | 97.0 ms                                                | 83.6 ms: 1.16x faster                                                 |
| pidigits       | 187 ms                                                 | 197 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.18x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.18 ms: 1.14x faster                                                 |
| regex_dna      | 212 ms                                                 | 196 ms: 1.08x faster                                                  |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.89 sec: 1.24x faster                                                |
| unpickle_pure_python | 230 us                                                 | 210 us: 1.09x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                  |
| json_loads           | 28.5 us                                                | 26.6 us: 1.07x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 57.8 ms: 1.07x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.2 ms: 1.05x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 162 ms: 1.01x slower                                                  |
| json_dumps           | 10.4 ms                                                | 12.1 ms: 1.16x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.98 ms: 1.01x slower                                                 |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 30.7 ms: 1.13x faster                                                 |
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 573 ms: 2.06x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 290 ms: 1.98x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 597 ms: 1.94x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 236 ms: 1.91x faster                                                  |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 467 ms: 1.55x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 482 ms: 1.51x faster                                                  |
| deepcopy                   | 371 us                                                 | 250 us: 1.49x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.40x faster                                                 |
| pathlib                    | 19.3 ms                                                | 14.2 ms: 1.36x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.1 us: 1.35x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 58.3 ms: 1.29x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.60 us: 1.29x faster                                                 |
| go                         | 139 ms                                                 | 109 ms: 1.28x faster                                                  |
| float                      | 84.7 ms                                                | 66.4 ms: 1.28x faster                                                 |
| scimark_fft                | 382 ms                                                 | 301 ms: 1.27x faster                                                  |
| spectral_norm              | 115 ms                                                 | 90.8 ms: 1.27x faster                                                 |
| deltablue                  | 3.72 ms                                                | 2.98 ms: 1.25x faster                                                 |
| raytrace                   | 312 ms                                                 | 252 ms: 1.24x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.09 ms: 1.24x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.89 sec: 1.24x faster                                                |
| chaos                      | 67.0 ms                                                | 54.2 ms: 1.23x faster                                                 |
| logging_format             | 7.23 us                                                | 6.03 us: 1.20x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.43 us: 1.19x faster                                                 |
| scimark_sor                | 129 ms                                                 | 109 ms: 1.19x faster                                                  |
| pyflate                    | 482 ms                                                 | 407 ms: 1.18x faster                                                  |
| regex_compile              | 148 ms                                                 | 125 ms: 1.18x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 69.4 ms: 1.18x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 144 ms: 1.17x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 101 ms: 1.17x faster                                                  |
| nbody                      | 97.0 ms                                                | 83.6 ms: 1.16x faster                                                 |
| sqlalchemy_declarative     | 147 ms                                                 | 127 ms: 1.16x faster                                                  |
| generators                 | 31.2 ms                                                | 27.1 ms: 1.15x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.19 ms: 1.15x faster                                                 |
| sympy_str                  | 300 ms                                                 | 261 ms: 1.15x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.4 ms: 1.14x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.18 ms: 1.14x faster                                                 |
| richards                   | 45.8 ms                                                | 40.4 ms: 1.14x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.50 ms: 1.13x faster                                                 |
| django_template            | 34.6 ms                                                | 30.7 ms: 1.13x faster                                                 |
| nqueens                    | 83.3 ms                                                | 74.1 ms: 1.12x faster                                                 |
| logging_silent             | 104 ns                                                 | 93.0 ns: 1.12x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.1 ms: 1.12x faster                                                 |
| hexiom                     | 6.41 ms                                                | 5.80 ms: 1.11x faster                                                 |
| 2to3                       | 274 ms                                                 | 249 ms: 1.10x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 62.4 ms: 1.10x faster                                                 |
| richards_super             | 51.5 ms                                                | 47.1 ms: 1.09x faster                                                 |
| coroutines                 | 23.2 ms                                                | 21.2 ms: 1.09x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 210 us: 1.09x faster                                                  |
| async_generators           | 463 ms                                                 | 427 ms: 1.08x faster                                                  |
| fannkuch                   | 417 ms                                                 | 386 ms: 1.08x faster                                                  |
| regex_dna                  | 212 ms                                                 | 196 ms: 1.08x faster                                                  |
| sympy_expand               | 478 ms                                                 | 444 ms: 1.08x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 103 ms: 1.07x faster                                                  |
| json                       | 5.26 ms                                                | 4.91 ms: 1.07x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                  |
| json_loads                 | 28.5 us                                                | 26.6 us: 1.07x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 57.8 ms: 1.07x faster                                                 |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 85.2 ms: 1.05x faster                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 52.4 ms: 1.05x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.72 us: 1.04x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 746 ms: 1.04x faster                                                  |
| typing_runtime_protocols   | 158 us                                                 | 154 us: 1.02x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 829 us: 1.02x faster                                                  |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.01x faster                                                  |
| python_startup_no_site     | 6.94 ms                                                | 6.98 ms: 1.01x slower                                                 |
| xml_etree_parse            | 159 ms                                                 | 162 ms: 1.01x slower                                                  |
| telco                      | 7.10 ms                                                | 7.29 ms: 1.03x slower                                                 |
| pidigits                   | 187 ms                                                 | 197 ms: 1.05x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                 |
| mdp                        | 2.63 sec                                               | 2.88 sec: 1.10x slower                                                |
| coverage                   | 72.7 ms                                                | 81.1 ms: 1.12x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 12.1 ms: 1.16x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.96 ms: 1.31x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.54 ms: 1.72x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 80.7 ms: 3.36x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.13x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250107-3.14.0a3+-f1d3190-CLANG/bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.154x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.10x