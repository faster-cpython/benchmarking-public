# Results vs. base

- fork: python
- ref: dbd23790dbd662169905
- machine: windows-amd64
- commit hash: dbd2379
- commit date: 2024-11-23
- overall geometric mean: 1.050x faster
- HPT reliability: 98.36%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241123-3.14.0a2+-dbd2379/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json | results/bm-20241123-3.14.0a2+-dbd2379-JIT/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| docutils       | 1.69 sec                                                                                                               | 1.79 sec: 1.06x slower                                                                                                     |
| html5lib       | 40.7 ms                                                                                                                | 39.0 ms: 1.04x faster                                                                                                      |
| sphinx         | 673 ms                                                                                                                 | 695 ms: 1.03x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.01x slower                                                                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | results/bm-20241123-3.14.0a2+-dbd2379/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json | results/bm-20241123-3.14.0a2+-dbd2379-JIT/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json |
|--------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none    | 213 ms                                                                                                                 | 209 ms: 1.02x faster                                                                                                       |
| asyncio_websockets | 302 ms                                                                                                                 | 308 ms: 1.02x slower                                                                                                       |
| async_generators   | 247 ms                                                                                                                 | 264 ms: 1.07x slower                                                                                                       |
| Geometric mean     | (ref)                                                                                                                  | 1.01x slower                                                                                                               |

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization, async_tree_cpu_io_mixed, coroutines, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241123-3.14.0a2+-dbd2379/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json | results/bm-20241123-3.14.0a2+-dbd2379-JIT/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                                                                                | 52.4 ms: 1.52x faster                                                                                                      |
| float          | 56.5 ms                                                                                                                | 47.2 ms: 1.20x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.22x faster                                                                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241123-3.14.0a2+-dbd2379/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json | results/bm-20241123-3.14.0a2+-dbd2379-JIT/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 90.1 ms                                                                                                                | 85.1 ms: 1.06x faster                                                                                                      |
| regex_effbot   | 1.44 ms                                                                                                                | 1.49 ms: 1.03x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.01x faster                                                                                                               |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241123-3.14.0a2+-dbd2379/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json | results/bm-20241123-3.14.0a2+-dbd2379-JIT/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 152 us                                                                                                                 | 108 us: 1.42x faster                                                                                                       |
| tomli_loads          | 1.58 sec                                                                                                               | 1.26 sec: 1.26x faster                                                                                                     |
| xml_etree_process    | 41.4 ms                                                                                                                | 35.8 ms: 1.16x faster                                                                                                      |
| xml_etree_generate   | 58.4 ms                                                                                                                | 50.7 ms: 1.15x faster                                                                                                      |
| pickle_pure_python   | 229 us                                                                                                                 | 211 us: 1.08x faster                                                                                                       |
| json_dumps           | 6.63 ms                                                                                                                | 6.27 ms: 1.06x faster                                                                                                      |
| xml_etree_iterparse  | 66.6 ms                                                                                                                | 63.5 ms: 1.05x faster                                                                                                      |
| xml_etree_parse      | 94.7 ms                                                                                                                | 93.7 ms: 1.01x faster                                                                                                      |
| json_loads           | 14.1 us                                                                                                                | 14.4 us: 1.02x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.12x faster                                                                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20241123-3.14.0a2+-dbd2379/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json | results/bm-20241123-3.14.0a2+-dbd2379-JIT/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 23.6 ms                                                                                                                | 23.2 ms: 1.02x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.01x faster                                                                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241123-3.14.0a2+-dbd2379/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json | results/bm-20241123-3.14.0a2+-dbd2379-JIT/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.00 ms                                                                                                                | 5.15 ms: 1.36x faster                                                                                                      |
| django_template | 24.9 ms                                                                                                                | 26.1 ms: 1.05x slower                                                                                                      |
| genshi_text     | 17.1 ms                                                                                                                | 18.4 ms: 1.07x slower                                                                                                      |
| genshi_xml      | 36.9 ms                                                                                                                | 44.3 ms: 1.20x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                  | 1.00x faster                                                                                                               |

All benchmarks:
===============

| Benchmark                | results/bm-20241123-3.14.0a2+-dbd2379/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json | results/bm-20241123-3.14.0a2+-dbd2379-JIT/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json |
|--------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody                    | 80.0 ms                                                                                                                | 52.4 ms: 1.52x faster                                                                                                      |
| unpickle_pure_python     | 152 us                                                                                                                 | 108 us: 1.42x faster                                                                                                       |
| scimark_sor              | 89.7 ms                                                                                                                | 64.1 ms: 1.40x faster                                                                                                      |
| deepcopy_memo            | 21.5 us                                                                                                                | 15.8 us: 1.37x faster                                                                                                      |
| mako                     | 7.00 ms                                                                                                                | 5.15 ms: 1.36x faster                                                                                                      |
| scimark_fft              | 201 ms                                                                                                                 | 153 ms: 1.32x faster                                                                                                       |
| scimark_monte_carlo      | 47.5 ms                                                                                                                | 36.4 ms: 1.30x faster                                                                                                      |
| spectral_norm            | 67.9 ms                                                                                                                | 53.3 ms: 1.27x faster                                                                                                      |
| tomli_loads              | 1.58 sec                                                                                                               | 1.26 sec: 1.26x faster                                                                                                     |
| scimark_sparse_mat_mult  | 2.71 ms                                                                                                                | 2.24 ms: 1.21x faster                                                                                                      |
| crypto_pyaes             | 48.8 ms                                                                                                                | 40.4 ms: 1.21x faster                                                                                                      |
| float                    | 56.5 ms                                                                                                                | 47.2 ms: 1.20x faster                                                                                                      |
| pprint_safe_repr         | 555 ms                                                                                                                 | 473 ms: 1.17x faster                                                                                                       |
| pprint_pformat           | 1.13 sec                                                                                                               | 970 ms: 1.16x faster                                                                                                       |
| scimark_lu               | 63.9 ms                                                                                                                | 55.2 ms: 1.16x faster                                                                                                      |
| xml_etree_process        | 41.4 ms                                                                                                                | 35.8 ms: 1.16x faster                                                                                                      |
| xml_etree_generate       | 58.4 ms                                                                                                                | 50.7 ms: 1.15x faster                                                                                                      |
| pyflate                  | 324 ms                                                                                                                 | 284 ms: 1.14x faster                                                                                                       |
| bpe_tokeniser            | 3.05 sec                                                                                                               | 2.69 sec: 1.13x faster                                                                                                     |
| fannkuch                 | 289 ms                                                                                                                 | 258 ms: 1.12x faster                                                                                                       |
| logging_silent           | 64.0 ns                                                                                                                | 57.5 ns: 1.11x faster                                                                                                      |
| chaos                    | 44.4 ms                                                                                                                | 40.5 ms: 1.10x faster                                                                                                      |
| telco                    | 4.75 ms                                                                                                                | 4.33 ms: 1.10x faster                                                                                                      |
| pickle_pure_python       | 229 us                                                                                                                 | 211 us: 1.08x faster                                                                                                       |
| meteor_contest           | 78.2 ms                                                                                                                | 72.4 ms: 1.08x faster                                                                                                      |
| regex_compile            | 90.1 ms                                                                                                                | 85.1 ms: 1.06x faster                                                                                                      |
| json_dumps               | 6.63 ms                                                                                                                | 6.27 ms: 1.06x faster                                                                                                      |
| k_core                   | 2.11 sec                                                                                                               | 2.01 sec: 1.05x faster                                                                                                     |
| sqlglot_parse            | 921 us                                                                                                                 | 878 us: 1.05x faster                                                                                                       |
| xml_etree_iterparse      | 66.6 ms                                                                                                                | 63.5 ms: 1.05x faster                                                                                                      |
| html5lib                 | 40.7 ms                                                                                                                | 39.0 ms: 1.04x faster                                                                                                      |
| dulwich_log              | 42.5 ms                                                                                                                | 40.7 ms: 1.04x faster                                                                                                      |
| connected_components     | 327 ms                                                                                                                 | 313 ms: 1.04x faster                                                                                                       |
| logging_simple           | 6.34 us                                                                                                                | 6.10 us: 1.04x faster                                                                                                      |
| pycparser                | 732 ms                                                                                                                 | 705 ms: 1.04x faster                                                                                                       |
| comprehensions           | 12.2 us                                                                                                                | 11.8 us: 1.04x faster                                                                                                      |
| logging_format           | 6.76 us                                                                                                                | 6.53 us: 1.04x faster                                                                                                      |
| json                     | 3.04 ms                                                                                                                | 2.97 ms: 1.02x faster                                                                                                      |
| deepcopy_reduce          | 1.92 us                                                                                                                | 1.88 us: 1.02x faster                                                                                                      |
| async_tree_none          | 213 ms                                                                                                                 | 209 ms: 1.02x faster                                                                                                       |
| nqueens                  | 64.5 ms                                                                                                                | 63.4 ms: 1.02x faster                                                                                                      |
| python_startup           | 23.6 ms                                                                                                                | 23.2 ms: 1.02x faster                                                                                                      |
| typing_runtime_protocols | 113 us                                                                                                                 | 112 us: 1.01x faster                                                                                                       |
| create_gc_cycles         | 1.33 ms                                                                                                                | 1.31 ms: 1.01x faster                                                                                                      |
| gc_traversal             | 1.87 ms                                                                                                                | 1.85 ms: 1.01x faster                                                                                                      |
| generators               | 22.4 ms                                                                                                                | 22.2 ms: 1.01x faster                                                                                                      |
| xml_etree_parse          | 94.7 ms                                                                                                                | 93.7 ms: 1.01x faster                                                                                                      |
| thrift                   | 535 us                                                                                                                 | 530 us: 1.01x faster                                                                                                       |
| deepcopy                 | 189 us                                                                                                                 | 188 us: 1.01x faster                                                                                                       |
| sqlglot_transpile        | 1.14 ms                                                                                                                | 1.13 ms: 1.01x faster                                                                                                      |
| pathlib                  | 76.1 ms                                                                                                                | 76.5 ms: 1.00x slower                                                                                                      |
| sympy_expand             | 304 ms                                                                                                                 | 307 ms: 1.01x slower                                                                                                       |
| coverage                 | 46.6 ms                                                                                                                | 47.0 ms: 1.01x slower                                                                                                      |
| sympy_str                | 177 ms                                                                                                                 | 179 ms: 1.01x slower                                                                                                       |
| mdp                      | 1.48 sec                                                                                                               | 1.50 sec: 1.02x slower                                                                                                     |
| json_loads               | 14.1 us                                                                                                                | 14.4 us: 1.02x slower                                                                                                      |
| asyncio_websockets       | 302 ms                                                                                                                 | 308 ms: 1.02x slower                                                                                                       |
| go                       | 89.7 ms                                                                                                                | 91.7 ms: 1.02x slower                                                                                                      |
| sqlite_synth             | 1.62 us                                                                                                                | 1.66 us: 1.02x slower                                                                                                      |
| sphinx                   | 673 ms                                                                                                                 | 695 ms: 1.03x slower                                                                                                       |
| regex_effbot             | 1.44 ms                                                                                                                | 1.49 ms: 1.03x slower                                                                                                      |
| raytrace                 | 202 ms                                                                                                                 | 209 ms: 1.03x slower                                                                                                       |
| sqlglot_optimize         | 36.5 ms                                                                                                                | 37.9 ms: 1.04x slower                                                                                                      |
| sympy_integrate          | 13.4 ms                                                                                                                | 13.9 ms: 1.04x slower                                                                                                      |
| django_template          | 24.9 ms                                                                                                                | 26.1 ms: 1.05x slower                                                                                                      |
| sympy_sum                | 89.4 ms                                                                                                                | 93.7 ms: 1.05x slower                                                                                                      |
| sqlglot_normalize        | 193 ms                                                                                                                 | 205 ms: 1.06x slower                                                                                                       |
| docutils                 | 1.69 sec                                                                                                               | 1.79 sec: 1.06x slower                                                                                                     |
| async_generators         | 247 ms                                                                                                                 | 264 ms: 1.07x slower                                                                                                       |
| many_optionals           | 446 us                                                                                                                 | 479 us: 1.07x slower                                                                                                       |
| genshi_text              | 17.1 ms                                                                                                                | 18.4 ms: 1.07x slower                                                                                                      |
| pylint                   | 189 ms                                                                                                                 | 207 ms: 1.09x slower                                                                                                       |
| hexiom                   | 4.49 ms                                                                                                                | 4.99 ms: 1.11x slower                                                                                                      |
| genshi_xml               | 36.9 ms                                                                                                                | 44.3 ms: 1.20x slower                                                                                                      |
| Geometric mean           | (ref)                                                                                                                  | 1.05x faster                                                                                                               |

Benchmark hidden because not significant (20): async_tree_none_tg, regex_v8, subparsers, shortest_path, async_tree_cpu_io_mixed_tg, python_startup_no_site, pidigits, richards_super, bench_thread_pool, async_tree_io_tg, deltablue, richards, bench_mp_pool, regex_dna, 2to3, async_tree_memoization, async_tree_cpu_io_mixed, coroutines, async_tree_memoization_tg, async_tree_io

- Geometric mean (including insignificant results): 1.050x faster
# HPT report

- Reliability score: 98.36% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown