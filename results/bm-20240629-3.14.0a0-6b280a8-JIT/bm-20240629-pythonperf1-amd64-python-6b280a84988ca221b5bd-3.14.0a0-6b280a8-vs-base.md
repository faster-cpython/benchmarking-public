# Results vs. base

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: windows-amd64
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.04x faster
- HPT reliability: 72.66%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-JIT/bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 226 ms                                                                                                               | 237 ms: 1.05x slower                                                                                                     |
| docutils       | 1.69 sec                                                                                                             | 1.77 sec: 1.05x slower                                                                                                   |
| html5lib       | 38.3 ms                                                                                                              | 38.9 ms: 1.02x slower                                                                                                    |
| tornado_http   | 82.1 ms                                                                                                              | 84.3 ms: 1.03x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.04x slower                                                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-JIT/bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io  | 569 ms                                                                                                               | 544 ms: 1.05x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.02x faster                                                                                                             |

Benchmark hidden because not significant (7): async_tree_none, async_tree_memoization, async_tree_io_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-JIT/bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 82.2 ms                                                                                                              | 51.4 ms: 1.60x faster                                                                                                    |
| float          | 57.4 ms                                                                                                              | 45.6 ms: 1.26x faster                                                                                                    |
| pidigits       | 150 ms                                                                                                               | 150 ms: 1.01x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.27x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-JIT/bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                                                                               | 121 ms: 1.02x slower                                                                                                     |
| regex_compile  | 88.1 ms                                                                                                              | 90.1 ms: 1.02x slower                                                                                                    |
| regex_v8       | 16.6 ms                                                                                                              | 20.1 ms: 1.21x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.06x slower                                                                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-JIT/bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.63 sec                                                                                                             | 1.29 sec: 1.27x faster                                                                                                   |
| pickle_pure_python   | 211 us                                                                                                               | 180 us: 1.17x faster                                                                                                     |
| xml_etree_generate   | 59.7 ms                                                                                                              | 53.8 ms: 1.11x faster                                                                                                    |
| unpickle_pure_python | 156 us                                                                                                               | 142 us: 1.10x faster                                                                                                     |
| xml_etree_process    | 42.0 ms                                                                                                              | 39.2 ms: 1.07x faster                                                                                                    |
| xml_etree_iterparse  | 66.6 ms                                                                                                              | 62.9 ms: 1.06x faster                                                                                                    |
| json_dumps           | 6.00 ms                                                                                                              | 5.89 ms: 1.02x faster                                                                                                    |
| json_loads           | 13.8 us                                                                                                              | 14.2 us: 1.03x slower                                                                                                    |
| xml_etree_parse      | 93.9 ms                                                                                                              | 97.6 ms: 1.04x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.08x faster                                                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-JIT/bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                                                                              | 22.5 ms: 1.09x slower                                                                                                    |
| python_startup_no_site | 17.0 ms                                                                                                              | 18.6 ms: 1.10x slower                                                                                                    |
| Geometric mean         | (ref)                                                                                                                | 1.09x slower                                                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-JIT/bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.85 ms                                                                                                              | 5.19 ms: 1.51x faster                                                                                                    |
| django_template | 24.3 ms                                                                                                              | 26.9 ms: 1.10x slower                                                                                                    |
| genshi_text     | 16.9 ms                                                                                                              | 18.7 ms: 1.11x slower                                                                                                    |
| genshi_xml      | 36.3 ms                                                                                                              | 44.9 ms: 1.24x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.00x slower                                                                                                             |

All benchmarks:
===============

| Benchmark                | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-JIT/bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|--------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| spectral_norm            | 73.2 ms                                                                                                              | 45.3 ms: 1.62x faster                                                                                                    |
| nbody                    | 82.2 ms                                                                                                              | 51.4 ms: 1.60x faster                                                                                                    |
| mako                     | 7.85 ms                                                                                                              | 5.19 ms: 1.51x faster                                                                                                    |
| scimark_sparse_mat_mult  | 3.07 ms                                                                                                              | 2.14 ms: 1.43x faster                                                                                                    |
| scimark_fft              | 215 ms                                                                                                               | 151 ms: 1.43x faster                                                                                                     |
| deepcopy_memo            | 21.6 us                                                                                                              | 15.8 us: 1.37x faster                                                                                                    |
| fannkuch                 | 303 ms                                                                                                               | 222 ms: 1.36x faster                                                                                                     |
| crypto_pyaes             | 52.6 ms                                                                                                              | 41.1 ms: 1.28x faster                                                                                                    |
| tomli_loads              | 1.63 sec                                                                                                             | 1.29 sec: 1.27x faster                                                                                                   |
| scimark_monte_carlo      | 50.0 ms                                                                                                              | 39.6 ms: 1.26x faster                                                                                                    |
| float                    | 57.4 ms                                                                                                              | 45.6 ms: 1.26x faster                                                                                                    |
| pyflate                  | 324 ms                                                                                                               | 264 ms: 1.23x faster                                                                                                     |
| pickle_pure_python       | 211 us                                                                                                               | 180 us: 1.17x faster                                                                                                     |
| comprehensions           | 12.0 us                                                                                                              | 10.5 us: 1.15x faster                                                                                                    |
| pprint_safe_repr         | 556 ms                                                                                                               | 490 ms: 1.13x faster                                                                                                     |
| pprint_pformat           | 1.13 sec                                                                                                             | 1.00 sec: 1.13x faster                                                                                                   |
| logging_silent           | 64.6 ns                                                                                                              | 58.1 ns: 1.11x faster                                                                                                    |
| xml_etree_generate       | 59.7 ms                                                                                                              | 53.8 ms: 1.11x faster                                                                                                    |
| unpickle_pure_python     | 156 us                                                                                                               | 142 us: 1.10x faster                                                                                                     |
| sqlglot_parse            | 902 us                                                                                                               | 823 us: 1.10x faster                                                                                                     |
| chaos                    | 44.6 ms                                                                                                              | 40.9 ms: 1.09x faster                                                                                                    |
| telco                    | 4.86 ms                                                                                                              | 4.52 ms: 1.08x faster                                                                                                    |
| xml_etree_process        | 42.0 ms                                                                                                              | 39.2 ms: 1.07x faster                                                                                                    |
| sqlglot_transpile        | 1.12 ms                                                                                                              | 1.05 ms: 1.07x faster                                                                                                    |
| xml_etree_iterparse      | 66.6 ms                                                                                                              | 62.9 ms: 1.06x faster                                                                                                    |
| logging_simple           | 6.28 us                                                                                                              | 5.99 us: 1.05x faster                                                                                                    |
| deepcopy_reduce          | 1.89 us                                                                                                              | 1.81 us: 1.05x faster                                                                                                    |
| async_tree_io            | 569 ms                                                                                                               | 544 ms: 1.05x faster                                                                                                     |
| meteor_contest           | 77.4 ms                                                                                                              | 74.1 ms: 1.04x faster                                                                                                    |
| logging_format           | 6.72 us                                                                                                              | 6.44 us: 1.04x faster                                                                                                    |
| thrift                   | 536 us                                                                                                               | 518 us: 1.03x faster                                                                                                     |
| json_dumps               | 6.00 ms                                                                                                              | 5.89 ms: 1.02x faster                                                                                                    |
| coroutines               | 14.8 ms                                                                                                              | 14.6 ms: 1.01x faster                                                                                                    |
| pidigits                 | 150 ms                                                                                                               | 150 ms: 1.01x faster                                                                                                     |
| deepcopy                 | 185 us                                                                                                               | 184 us: 1.00x faster                                                                                                     |
| create_gc_cycles         | 895 us                                                                                                               | 907 us: 1.01x slower                                                                                                     |
| html5lib                 | 38.3 ms                                                                                                              | 38.9 ms: 1.02x slower                                                                                                    |
| generators               | 23.6 ms                                                                                                              | 24.0 ms: 1.02x slower                                                                                                    |
| regex_dna                | 118 ms                                                                                                               | 121 ms: 1.02x slower                                                                                                     |
| coverage                 | 45.4 ms                                                                                                              | 46.4 ms: 1.02x slower                                                                                                    |
| regex_compile            | 88.1 ms                                                                                                              | 90.1 ms: 1.02x slower                                                                                                    |
| tornado_http             | 82.1 ms                                                                                                              | 84.3 ms: 1.03x slower                                                                                                    |
| json_loads               | 13.8 us                                                                                                              | 14.2 us: 1.03x slower                                                                                                    |
| go                       | 95.1 ms                                                                                                              | 97.8 ms: 1.03x slower                                                                                                    |
| sqlglot_optimize         | 35.6 ms                                                                                                              | 37.0 ms: 1.04x slower                                                                                                    |
| raytrace                 | 180 ms                                                                                                               | 186 ms: 1.04x slower                                                                                                     |
| xml_etree_parse          | 93.9 ms                                                                                                              | 97.6 ms: 1.04x slower                                                                                                    |
| sympy_sum                | 88.9 ms                                                                                                              | 93.1 ms: 1.05x slower                                                                                                    |
| sqlglot_normalize        | 191 ms                                                                                                               | 200 ms: 1.05x slower                                                                                                     |
| typing_runtime_protocols | 112 us                                                                                                               | 118 us: 1.05x slower                                                                                                     |
| 2to3                     | 226 ms                                                                                                               | 237 ms: 1.05x slower                                                                                                     |
| docutils                 | 1.69 sec                                                                                                             | 1.77 sec: 1.05x slower                                                                                                   |
| scimark_sor              | 89.4 ms                                                                                                              | 94.3 ms: 1.05x slower                                                                                                    |
| sympy_str                | 172 ms                                                                                                               | 182 ms: 1.06x slower                                                                                                     |
| deltablue                | 2.24 ms                                                                                                              | 2.37 ms: 1.06x slower                                                                                                    |
| richards                 | 30.9 ms                                                                                                              | 32.7 ms: 1.06x slower                                                                                                    |
| richards_super           | 34.7 ms                                                                                                              | 36.9 ms: 1.06x slower                                                                                                    |
| hexiom                   | 4.50 ms                                                                                                              | 4.80 ms: 1.07x slower                                                                                                    |
| bench_mp_pool            | 65.8 ms                                                                                                              | 70.2 ms: 1.07x slower                                                                                                    |
| sympy_integrate          | 13.2 ms                                                                                                              | 14.1 ms: 1.07x slower                                                                                                    |
| sympy_expand             | 292 ms                                                                                                               | 316 ms: 1.08x slower                                                                                                     |
| python_startup           | 20.6 ms                                                                                                              | 22.5 ms: 1.09x slower                                                                                                    |
| async_generators         | 248 ms                                                                                                               | 271 ms: 1.09x slower                                                                                                     |
| python_startup_no_site   | 17.0 ms                                                                                                              | 18.6 ms: 1.10x slower                                                                                                    |
| django_template          | 24.3 ms                                                                                                              | 26.9 ms: 1.10x slower                                                                                                    |
| genshi_text              | 16.9 ms                                                                                                              | 18.7 ms: 1.11x slower                                                                                                    |
| pylint                   | 213 ms                                                                                                               | 237 ms: 1.11x slower                                                                                                     |
| scimark_lu               | 67.0 ms                                                                                                              | 75.0 ms: 1.12x slower                                                                                                    |
| regex_v8                 | 16.6 ms                                                                                                              | 20.1 ms: 1.21x slower                                                                                                    |
| genshi_xml               | 36.3 ms                                                                                                              | 44.9 ms: 1.24x slower                                                                                                    |
| Geometric mean           | (ref)                                                                                                                | 1.04x faster                                                                                                             |

Benchmark hidden because not significant (17): json, async_tree_none, async_tree_memoization, asyncio_tcp, async_tree_io_tg, async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_tcp_ssl, nqueens, pathlib, regex_effbot, async_tree_cpu_io_mixed_tg, gc_traversal, mdp, async_tree_memoization_tg, bench_thread_pool, pycparser

# HPT report

- Reliability score: 72.66% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown