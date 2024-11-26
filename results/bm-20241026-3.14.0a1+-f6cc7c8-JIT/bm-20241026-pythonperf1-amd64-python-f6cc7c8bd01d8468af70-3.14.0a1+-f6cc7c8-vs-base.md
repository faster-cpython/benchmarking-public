# Results vs. base

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: windows-amd64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.029x faster
- HPT reliability: 50.54%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 230 ms                                                                                                                 | 250 ms: 1.09x slower                                                                                                       |
| docutils       | 1.72 sec                                                                                                               | 1.92 sec: 1.12x slower                                                                                                     |
| html5lib       | 42.0 ms                                                                                                                | 38.8 ms: 1.08x faster                                                                                                      |
| sphinx         | 674 ms                                                                                                                 | 767 ms: 1.14x slower                                                                                                       |
| tornado_http   | 93.0 ms                                                                                                                | 98.7 ms: 1.06x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.06x slower                                                                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|-------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg        | 644 ms                                                                                                                 | 604 ms: 1.07x faster                                                                                                       |
| async_tree_io           | 564 ms                                                                                                                 | 539 ms: 1.05x faster                                                                                                       |
| async_tree_memoization  | 278 ms                                                                                                                 | 266 ms: 1.05x faster                                                                                                       |
| coroutines              | 14.1 ms                                                                                                                | 14.4 ms: 1.02x slower                                                                                                      |
| async_tree_cpu_io_mixed | 386 ms                                                                                                                 | 396 ms: 1.03x slower                                                                                                       |
| async_tree_none_tg      | 211 ms                                                                                                                 | 221 ms: 1.05x slower                                                                                                       |
| async_generators        | 242 ms                                                                                                                 | 267 ms: 1.10x slower                                                                                                       |
| Geometric mean          | (ref)                                                                                                                  | 1.00x slower                                                                                                               |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 78.1 ms                                                                                                                | 53.7 ms: 1.45x faster                                                                                                      |
| float          | 54.9 ms                                                                                                                | 47.4 ms: 1.16x faster                                                                                                      |
| pidigits       | 148 ms                                                                                                                 | 149 ms: 1.01x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.19x faster                                                                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                                                                                 | 121 ms: 1.03x slower                                                                                                       |
| regex_effbot   | 1.57 ms                                                                                                                | 1.63 ms: 1.04x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.01x slower                                                                                                               |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.60 sec                                                                                                               | 1.28 sec: 1.25x faster                                                                                                     |
| xml_etree_generate   | 57.8 ms                                                                                                                | 50.5 ms: 1.14x faster                                                                                                      |
| xml_etree_process    | 40.3 ms                                                                                                                | 36.2 ms: 1.11x faster                                                                                                      |
| json_dumps           | 6.84 ms                                                                                                                | 6.18 ms: 1.11x faster                                                                                                      |
| pickle_pure_python   | 223 us                                                                                                                 | 204 us: 1.09x faster                                                                                                       |
| json_loads           | 15.5 us                                                                                                                | 14.6 us: 1.07x faster                                                                                                      |
| xml_etree_iterparse  | 66.7 ms                                                                                                                | 63.1 ms: 1.06x faster                                                                                                      |
| unpickle_pure_python | 150 us                                                                                                                 | 144 us: 1.04x faster                                                                                                       |
| xml_etree_parse      | 96.9 ms                                                                                                                | 95.9 ms: 1.01x faster                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.10x faster                                                                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                                                                                | 18.4 ms: 1.01x slower                                                                                                      |
| Geometric mean         | (ref)                                                                                                                  | 1.01x slower                                                                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.82 ms                                                                                                                | 5.06 ms: 1.35x faster                                                                                                      |
| django_template | 25.5 ms                                                                                                                | 27.0 ms: 1.06x slower                                                                                                      |
| genshi_text     | 17.8 ms                                                                                                                | 19.2 ms: 1.08x slower                                                                                                      |
| genshi_xml      | 37.9 ms                                                                                                                | 46.3 ms: 1.22x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                  | 1.01x slower                                                                                                               |

All benchmarks:
===============

| Benchmark                | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|--------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody                    | 78.1 ms                                                                                                                | 53.7 ms: 1.45x faster                                                                                                      |
| scimark_sor              | 90.6 ms                                                                                                                | 64.9 ms: 1.39x faster                                                                                                      |
| mako                     | 6.82 ms                                                                                                                | 5.06 ms: 1.35x faster                                                                                                      |
| scimark_fft              | 209 ms                                                                                                                 | 155 ms: 1.34x faster                                                                                                       |
| scimark_monte_carlo      | 47.1 ms                                                                                                                | 37.2 ms: 1.26x faster                                                                                                      |
| tomli_loads              | 1.60 sec                                                                                                               | 1.28 sec: 1.25x faster                                                                                                     |
| scimark_sparse_mat_mult  | 2.73 ms                                                                                                                | 2.23 ms: 1.23x faster                                                                                                      |
| crypto_pyaes             | 49.1 ms                                                                                                                | 40.5 ms: 1.21x faster                                                                                                      |
| pprint_safe_repr         | 562 ms                                                                                                                 | 468 ms: 1.20x faster                                                                                                       |
| deepcopy_memo            | 20.1 us                                                                                                                | 16.8 us: 1.20x faster                                                                                                      |
| spectral_norm            | 68.3 ms                                                                                                                | 57.6 ms: 1.19x faster                                                                                                      |
| fannkuch                 | 283 ms                                                                                                                 | 240 ms: 1.18x faster                                                                                                       |
| pprint_pformat           | 1.12 sec                                                                                                               | 950 ms: 1.18x faster                                                                                                       |
| float                    | 54.9 ms                                                                                                                | 47.4 ms: 1.16x faster                                                                                                      |
| xml_etree_generate       | 57.8 ms                                                                                                                | 50.5 ms: 1.14x faster                                                                                                      |
| xml_etree_process        | 40.3 ms                                                                                                                | 36.2 ms: 1.11x faster                                                                                                      |
| json_dumps               | 6.84 ms                                                                                                                | 6.18 ms: 1.11x faster                                                                                                      |
| pyflate                  | 323 ms                                                                                                                 | 292 ms: 1.11x faster                                                                                                       |
| json                     | 3.20 ms                                                                                                                | 2.92 ms: 1.09x faster                                                                                                      |
| pickle_pure_python       | 223 us                                                                                                                 | 204 us: 1.09x faster                                                                                                       |
| scimark_lu               | 61.2 ms                                                                                                                | 56.2 ms: 1.09x faster                                                                                                      |
| html5lib                 | 42.0 ms                                                                                                                | 38.8 ms: 1.08x faster                                                                                                      |
| dulwich_log              | 43.7 ms                                                                                                                | 40.4 ms: 1.08x faster                                                                                                      |
| telco                    | 4.87 ms                                                                                                                | 4.53 ms: 1.08x faster                                                                                                      |
| chaos                    | 43.8 ms                                                                                                                | 40.9 ms: 1.07x faster                                                                                                      |
| comprehensions           | 12.5 us                                                                                                                | 11.7 us: 1.07x faster                                                                                                      |
| async_tree_io_tg         | 644 ms                                                                                                                 | 604 ms: 1.07x faster                                                                                                       |
| json_loads               | 15.5 us                                                                                                                | 14.6 us: 1.07x faster                                                                                                      |
| logging_silent           | 62.2 ns                                                                                                                | 58.4 ns: 1.06x faster                                                                                                      |
| xml_etree_iterparse      | 66.7 ms                                                                                                                | 63.1 ms: 1.06x faster                                                                                                      |
| async_tree_io            | 564 ms                                                                                                                 | 539 ms: 1.05x faster                                                                                                       |
| logging_format           | 6.95 us                                                                                                                | 6.63 us: 1.05x faster                                                                                                      |
| async_tree_memoization   | 278 ms                                                                                                                 | 266 ms: 1.05x faster                                                                                                       |
| unpickle_pure_python     | 150 us                                                                                                                 | 144 us: 1.04x faster                                                                                                       |
| sqlglot_parse            | 922 us                                                                                                                 | 886 us: 1.04x faster                                                                                                       |
| logging_simple           | 6.51 us                                                                                                                | 6.30 us: 1.03x faster                                                                                                      |
| deepcopy_reduce          | 1.94 us                                                                                                                | 1.88 us: 1.03x faster                                                                                                      |
| meteor_contest           | 76.8 ms                                                                                                                | 74.7 ms: 1.03x faster                                                                                                      |
| deepcopy                 | 193 us                                                                                                                 | 190 us: 1.02x faster                                                                                                       |
| thrift                   | 538 us                                                                                                                 | 532 us: 1.01x faster                                                                                                       |
| xml_etree_parse          | 96.9 ms                                                                                                                | 95.9 ms: 1.01x faster                                                                                                      |
| pycparser                | 734 ms                                                                                                                 | 727 ms: 1.01x faster                                                                                                       |
| coverage                 | 49.3 ms                                                                                                                | 49.0 ms: 1.01x faster                                                                                                      |
| pidigits                 | 148 ms                                                                                                                 | 149 ms: 1.01x slower                                                                                                       |
| pathlib                  | 80.5 ms                                                                                                                | 81.2 ms: 1.01x slower                                                                                                      |
| gc_traversal             | 1.93 ms                                                                                                                | 1.95 ms: 1.01x slower                                                                                                      |
| nqueens                  | 63.2 ms                                                                                                                | 64.1 ms: 1.01x slower                                                                                                      |
| python_startup_no_site   | 18.1 ms                                                                                                                | 18.4 ms: 1.01x slower                                                                                                      |
| coroutines               | 14.1 ms                                                                                                                | 14.4 ms: 1.02x slower                                                                                                      |
| async_tree_cpu_io_mixed  | 386 ms                                                                                                                 | 396 ms: 1.03x slower                                                                                                       |
| sqlglot_transpile        | 1.14 ms                                                                                                                | 1.18 ms: 1.03x slower                                                                                                      |
| regex_dna                | 117 ms                                                                                                                 | 121 ms: 1.03x slower                                                                                                       |
| deltablue                | 2.27 ms                                                                                                                | 2.34 ms: 1.03x slower                                                                                                      |
| typing_runtime_protocols | 112 us                                                                                                                 | 116 us: 1.03x slower                                                                                                       |
| regex_effbot             | 1.57 ms                                                                                                                | 1.63 ms: 1.04x slower                                                                                                      |
| go                       | 88.0 ms                                                                                                                | 91.8 ms: 1.04x slower                                                                                                      |
| mdp                      | 1.56 sec                                                                                                               | 1.63 sec: 1.04x slower                                                                                                     |
| async_tree_none_tg       | 211 ms                                                                                                                 | 221 ms: 1.05x slower                                                                                                       |
| generators               | 21.7 ms                                                                                                                | 22.9 ms: 1.05x slower                                                                                                      |
| bench_mp_pool            | 84.6 ms                                                                                                                | 89.3 ms: 1.06x slower                                                                                                      |
| sqlglot_normalize        | 199 ms                                                                                                                 | 210 ms: 1.06x slower                                                                                                       |
| django_template          | 25.5 ms                                                                                                                | 27.0 ms: 1.06x slower                                                                                                      |
| raytrace                 | 196 ms                                                                                                                 | 208 ms: 1.06x slower                                                                                                       |
| tornado_http             | 93.0 ms                                                                                                                | 98.7 ms: 1.06x slower                                                                                                      |
| sympy_expand             | 306 ms                                                                                                                 | 326 ms: 1.07x slower                                                                                                       |
| sympy_str                | 179 ms                                                                                                                 | 191 ms: 1.07x slower                                                                                                       |
| richards                 | 32.2 ms                                                                                                                | 34.4 ms: 1.07x slower                                                                                                      |
| genshi_text              | 17.8 ms                                                                                                                | 19.2 ms: 1.08x slower                                                                                                      |
| richards_super           | 35.8 ms                                                                                                                | 38.5 ms: 1.08x slower                                                                                                      |
| 2to3                     | 230 ms                                                                                                                 | 250 ms: 1.09x slower                                                                                                       |
| async_generators         | 242 ms                                                                                                                 | 267 ms: 1.10x slower                                                                                                       |
| docutils                 | 1.72 sec                                                                                                               | 1.92 sec: 1.12x slower                                                                                                     |
| sphinx                   | 674 ms                                                                                                                 | 767 ms: 1.14x slower                                                                                                       |
| sympy_sum                | 89.7 ms                                                                                                                | 103 ms: 1.15x slower                                                                                                       |
| sqlglot_optimize         | 36.9 ms                                                                                                                | 42.9 ms: 1.16x slower                                                                                                      |
| sympy_integrate          | 13.5 ms                                                                                                                | 15.7 ms: 1.17x slower                                                                                                      |
| hexiom                   | 4.40 ms                                                                                                                | 5.26 ms: 1.20x slower                                                                                                      |
| genshi_xml               | 37.9 ms                                                                                                                | 46.3 ms: 1.22x slower                                                                                                      |
| pylint                   | 229 ms                                                                                                                 | 281 ms: 1.23x slower                                                                                                       |
| Geometric mean           | (ref)                                                                                                                  | 1.03x faster                                                                                                               |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, regex_v8, bench_thread_pool, regex_compile, python_startup, async_tree_none, create_gc_cycles, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.029x faster
# HPT report

- Reliability score: 50.54% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown