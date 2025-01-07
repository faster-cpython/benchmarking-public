# Results vs. base

- fork: kumaraditya303
- ref: future_iter
- machine: linux-x86_64
- commit hash: 82b905d
- commit date: 2025-01-05
- overall geometric mean: 1.002x slower
- HPT reliability: 98.59%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                 | 257 ms: 1.01x slower                                                  |
| docutils       | 2.61 sec                                                               | 2.64 sec: 1.01x slower                                                |
| html5lib       | 61.3 ms                                                                | 62.4 ms: 1.02x slower                                                 |
| sphinx         | 1.01 sec                                                               | 1.02 sec: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 611 ms                                                                 | 588 ms: 1.04x faster                                                  |
| async_tree_none         | 264 ms                                                                 | 259 ms: 1.02x faster                                                  |
| coroutines              | 23.7 ms                                                                | 23.2 ms: 1.02x faster                                                 |
| async_tree_memoization  | 330 ms                                                                 | 326 ms: 1.01x faster                                                  |
| async_generators        | 420 ms                                                                 | 416 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed | 481 ms                                                                 | 488 ms: 1.01x slower                                                  |
| async_tree_none_tg      | 243 ms                                                                 | 248 ms: 1.02x slower                                                  |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (4): async_tree_memoization_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 98.6 ms                                                                | 94.1 ms: 1.05x faster                                                 |
| float          | 73.8 ms                                                                | 72.5 ms: 1.02x faster                                                 |
| pidigits       | 189 ms                                                                 | 190 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                  |
| regex_v8       | 25.7 ms                                                                | 26.1 ms: 1.02x slower                                                 |
| regex_effbot   | 3.40 ms                                                                | 3.47 ms: 1.02x slower                                                 |
| regex_dna      | 214 ms                                                                 | 221 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 139 ms                                                                 | 137 ms: 1.01x faster                                                  |
| unpickle_pure_python | 220 us                                                                 | 217 us: 1.01x faster                                                  |
| xml_etree_generate   | 86.0 ms                                                                | 85.1 ms: 1.01x faster                                                 |
| xml_etree_iterparse  | 97.5 ms                                                                | 96.6 ms: 1.01x faster                                                 |
| pickle_pure_python   | 322 us                                                                 | 323 us: 1.00x slower                                                  |
| json_loads           | 26.3 us                                                                | 26.5 us: 1.01x slower                                                 |
| json_dumps           | 11.3 ms                                                                | 11.4 ms: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_process, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.07 ms                                                                | 7.05 ms: 1.00x faster                                                 |
| python_startup         | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.7 ms                                                                | 11.4 ms: 1.03x faster                                                 |
| genshi_text     | 22.5 ms                                                                | 22.4 ms: 1.00x faster                                                 |
| django_template | 31.6 ms                                                                | 31.5 ms: 1.00x faster                                                 |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody                   | 98.6 ms                                                                | 94.1 ms: 1.05x faster                                                 |
| async_tree_io           | 611 ms                                                                 | 588 ms: 1.04x faster                                                  |
| mako                    | 11.7 ms                                                                | 11.4 ms: 1.03x faster                                                 |
| async_tree_none         | 264 ms                                                                 | 259 ms: 1.02x faster                                                  |
| generators              | 28.2 ms                                                                | 27.6 ms: 1.02x faster                                                 |
| coroutines              | 23.7 ms                                                                | 23.2 ms: 1.02x faster                                                 |
| float                   | 73.8 ms                                                                | 72.5 ms: 1.02x faster                                                 |
| scimark_sparse_mat_mult | 4.83 ms                                                                | 4.77 ms: 1.01x faster                                                 |
| spectral_norm           | 105 ms                                                                 | 103 ms: 1.01x faster                                                  |
| xml_etree_parse         | 139 ms                                                                 | 137 ms: 1.01x faster                                                  |
| coverage                | 84.6 ms                                                                | 83.6 ms: 1.01x faster                                                 |
| unpickle_pure_python    | 220 us                                                                 | 217 us: 1.01x faster                                                  |
| async_tree_memoization  | 330 ms                                                                 | 326 ms: 1.01x faster                                                  |
| richards_super          | 51.4 ms                                                                | 50.9 ms: 1.01x faster                                                 |
| xml_etree_generate      | 86.0 ms                                                                | 85.1 ms: 1.01x faster                                                 |
| xml_etree_iterparse     | 97.5 ms                                                                | 96.6 ms: 1.01x faster                                                 |
| mdp                     | 2.71 sec                                                               | 2.68 sec: 1.01x faster                                                |
| richards                | 44.8 ms                                                                | 44.4 ms: 1.01x faster                                                 |
| scimark_monte_carlo     | 68.7 ms                                                                | 68.0 ms: 1.01x faster                                                 |
| comprehensions          | 17.3 us                                                                | 17.1 us: 1.01x faster                                                 |
| sqlglot_transpile       | 1.60 ms                                                                | 1.59 ms: 1.01x faster                                                 |
| async_generators        | 420 ms                                                                 | 416 ms: 1.01x faster                                                  |
| crypto_pyaes            | 71.8 ms                                                                | 71.3 ms: 1.01x faster                                                 |
| scimark_sor             | 124 ms                                                                 | 123 ms: 1.01x faster                                                  |
| genshi_text             | 22.5 ms                                                                | 22.4 ms: 1.00x faster                                                 |
| django_template         | 31.6 ms                                                                | 31.5 ms: 1.00x faster                                                 |
| scimark_fft             | 351 ms                                                                 | 350 ms: 1.00x faster                                                  |
| python_startup_no_site  | 7.07 ms                                                                | 7.05 ms: 1.00x faster                                                 |
| python_startup          | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                 |
| gc_traversal            | 4.78 ms                                                                | 4.78 ms: 1.00x slower                                                 |
| dulwich_log             | 64.0 ms                                                                | 64.2 ms: 1.00x slower                                                 |
| bench_thread_pool       | 866 us                                                                 | 869 us: 1.00x slower                                                  |
| raytrace                | 271 ms                                                                 | 272 ms: 1.00x slower                                                  |
| create_gc_cycles        | 2.44 ms                                                                | 2.45 ms: 1.00x slower                                                 |
| meteor_contest          | 108 ms                                                                 | 108 ms: 1.00x slower                                                  |
| deepcopy                | 260 us                                                                 | 261 us: 1.00x slower                                                  |
| pickle_pure_python      | 322 us                                                                 | 323 us: 1.00x slower                                                  |
| pidigits                | 189 ms                                                                 | 190 ms: 1.00x slower                                                  |
| nqueens                 | 79.8 ms                                                                | 80.3 ms: 1.01x slower                                                 |
| json_loads              | 26.3 us                                                                | 26.5 us: 1.01x slower                                                 |
| 2to3                    | 255 ms                                                                 | 257 ms: 1.01x slower                                                  |
| json_dumps              | 11.3 ms                                                                | 11.4 ms: 1.01x slower                                                 |
| sympy_str               | 269 ms                                                                 | 271 ms: 1.01x slower                                                  |
| sqlalchemy_declarative  | 129 ms                                                                 | 130 ms: 1.01x slower                                                  |
| pprint_safe_repr        | 728 ms                                                                 | 734 ms: 1.01x slower                                                  |
| regex_compile           | 128 ms                                                                 | 129 ms: 1.01x slower                                                  |
| pathlib                 | 16.1 ms                                                                | 16.2 ms: 1.01x slower                                                 |
| subparsers              | 20.8 ms                                                                | 21.0 ms: 1.01x slower                                                 |
| sqlalchemy_imperative   | 16.6 ms                                                                | 16.8 ms: 1.01x slower                                                 |
| deltablue               | 3.25 ms                                                                | 3.28 ms: 1.01x slower                                                 |
| deepcopy_memo           | 31.2 us                                                                | 31.5 us: 1.01x slower                                                 |
| bpe_tokeniser           | 4.51 sec                                                               | 4.55 sec: 1.01x slower                                                |
| scimark_lu              | 117 ms                                                                 | 118 ms: 1.01x slower                                                  |
| docutils                | 2.61 sec                                                               | 2.64 sec: 1.01x slower                                                |
| shortest_path           | 476 ms                                                                 | 482 ms: 1.01x slower                                                  |
| sphinx                  | 1.01 sec                                                               | 1.02 sec: 1.01x slower                                                |
| sympy_expand            | 454 ms                                                                 | 460 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed | 481 ms                                                                 | 488 ms: 1.01x slower                                                  |
| sympy_sum               | 147 ms                                                                 | 150 ms: 1.01x slower                                                  |
| logging_simple          | 5.68 us                                                                | 5.76 us: 1.01x slower                                                 |
| json                    | 4.88 ms                                                                | 4.95 ms: 1.01x slower                                                 |
| thrift                  | 768 us                                                                 | 780 us: 1.02x slower                                                  |
| regex_v8                | 25.7 ms                                                                | 26.1 ms: 1.02x slower                                                 |
| chaos                   | 60.2 ms                                                                | 61.2 ms: 1.02x slower                                                 |
| html5lib                | 61.3 ms                                                                | 62.4 ms: 1.02x slower                                                 |
| go                      | 117 ms                                                                 | 119 ms: 1.02x slower                                                  |
| regex_effbot            | 3.40 ms                                                                | 3.47 ms: 1.02x slower                                                 |
| pprint_pformat          | 1.48 sec                                                               | 1.51 sec: 1.02x slower                                                |
| async_tree_none_tg      | 243 ms                                                                 | 248 ms: 1.02x slower                                                  |
| fannkuch                | 401 ms                                                                 | 410 ms: 1.02x slower                                                  |
| hexiom                  | 6.21 ms                                                                | 6.39 ms: 1.03x slower                                                 |
| regex_dna               | 214 ms                                                                 | 221 ms: 1.03x slower                                                  |
| pyflate                 | 457 ms                                                                 | 474 ms: 1.04x slower                                                  |
| pycparser               | 1.13 sec                                                               | 1.18 sec: 1.05x slower                                                |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (23): telco, async_tree_memoization_tg, logging_silent, sqlite_synth, genshi_xml, sqlglot_parse, sqlglot_optimize, many_optionals, typing_runtime_protocols, xml_etree_process, deepcopy_reduce, asyncio_websockets, async_tree_cpu_io_mixed_tg, bench_mp_pool, tomli_loads, sympy_integrate, sqlglot_normalize, async_tree_io_tg, k_core, connected_components, logging_format, mypy2, pylint

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 98.59% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x