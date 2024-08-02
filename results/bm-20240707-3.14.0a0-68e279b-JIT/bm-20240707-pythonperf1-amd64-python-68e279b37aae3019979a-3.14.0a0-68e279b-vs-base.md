# Results vs. base

- fork: python
- ref: 68e279b37aae3019979a
- machine: windows-amd64
- commit hash: 68e279b
- commit date: 2024-07-07
- overall geometric mean: 1.00x slower
- HPT reliability: 92.12%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240707-3.14.0a0-68e279b/bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json | results/bm-20240707-3.14.0a0-68e279b-JIT/bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 214 ms                                                                                                               | 230 ms: 1.08x slower                                                                                                     |
| docutils       | 1.63 sec                                                                                                             | 1.74 sec: 1.07x slower                                                                                                   |
| html5lib       | 36.4 ms                                                                                                              | 38.1 ms: 1.05x slower                                                                                                    |
| tornado_http   | 80.9 ms                                                                                                              | 84.4 ms: 1.04x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.06x slower                                                                                                             |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240707-3.14.0a0-68e279b/bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json | results/bm-20240707-3.14.0a0-68e279b-JIT/bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 73.2 ms                                                                                                              | 52.2 ms: 1.40x faster                                                                                                    |
| float          | 52.6 ms                                                                                                              | 45.0 ms: 1.17x faster                                                                                                    |
| pidigits       | 150 ms                                                                                                               | 149 ms: 1.01x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.18x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240707-3.14.0a0-68e279b/bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json | results/bm-20240707-3.14.0a0-68e279b-JIT/bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 122 ms                                                                                                               | 116 ms: 1.05x faster                                                                                                     |
| regex_effbot   | 1.59 ms                                                                                                              | 1.57 ms: 1.02x faster                                                                                                    |
| regex_compile  | 78.5 ms                                                                                                              | 87.7 ms: 1.12x slower                                                                                                    |
| regex_v8       | 17.1 ms                                                                                                              | 19.9 ms: 1.17x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.05x slower                                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240707-3.14.0a0-68e279b/bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json | results/bm-20240707-3.14.0a0-68e279b-JIT/bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                                                                             | 1.25 sec: 1.17x faster                                                                                                   |
| pickle_pure_python   | 186 us                                                                                                               | 174 us: 1.07x faster                                                                                                     |
| xml_etree_generate   | 55.0 ms                                                                                                              | 51.8 ms: 1.06x faster                                                                                                    |
| xml_etree_iterparse  | 63.8 ms                                                                                                              | 60.9 ms: 1.05x faster                                                                                                    |
| unpickle_pure_python | 133 us                                                                                                               | 127 us: 1.05x faster                                                                                                     |
| xml_etree_process    | 37.8 ms                                                                                                              | 37.1 ms: 1.02x faster                                                                                                    |
| json_loads           | 14.0 us                                                                                                              | 14.2 us: 1.01x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.04x faster                                                                                                             |

Benchmark hidden because not significant (2): xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240707-3.14.0a0-68e279b/bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json | results/bm-20240707-3.14.0a0-68e279b-JIT/bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 20.9 ms                                                                                                              | 21.1 ms: 1.01x slower                                                                                                    |
| python_startup_no_site | 16.7 ms                                                                                                              | 17.4 ms: 1.04x slower                                                                                                    |
| Geometric mean         | (ref)                                                                                                                | 1.03x slower                                                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240707-3.14.0a0-68e279b/bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json | results/bm-20240707-3.14.0a0-68e279b-JIT/bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.59 ms                                                                                                              | 5.10 ms: 1.29x faster                                                                                                    |
| django_template | 23.2 ms                                                                                                              | 27.1 ms: 1.17x slower                                                                                                    |
| genshi_text     | 15.1 ms                                                                                                              | 17.9 ms: 1.19x slower                                                                                                    |
| genshi_xml      | 33.1 ms                                                                                                              | 44.2 ms: 1.33x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.09x slower                                                                                                             |

All benchmarks:
===============

| Benchmark                | results/bm-20240707-3.14.0a0-68e279b/bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json | results/bm-20240707-3.14.0a0-68e279b-JIT/bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json |
|--------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody                    | 73.2 ms                                                                                                              | 52.2 ms: 1.40x faster                                                                                                    |
| spectral_norm            | 62.3 ms                                                                                                              | 45.7 ms: 1.36x faster                                                                                                    |
| mako                     | 6.59 ms                                                                                                              | 5.10 ms: 1.29x faster                                                                                                    |
| scimark_fft              | 185 ms                                                                                                               | 149 ms: 1.24x faster                                                                                                     |
| scimark_sparse_mat_mult  | 2.64 ms                                                                                                              | 2.15 ms: 1.22x faster                                                                                                    |
| fannkuch                 | 273 ms                                                                                                               | 230 ms: 1.19x faster                                                                                                     |
| deepcopy_memo            | 18.6 us                                                                                                              | 15.7 us: 1.18x faster                                                                                                    |
| tomli_loads              | 1.47 sec                                                                                                             | 1.25 sec: 1.17x faster                                                                                                   |
| asyncio_tcp_ssl          | 1.60 sec                                                                                                             | 1.36 sec: 1.17x faster                                                                                                   |
| float                    | 52.6 ms                                                                                                              | 45.0 ms: 1.17x faster                                                                                                    |
| scimark_monte_carlo      | 43.6 ms                                                                                                              | 37.9 ms: 1.15x faster                                                                                                    |
| crypto_pyaes             | 46.8 ms                                                                                                              | 41.1 ms: 1.14x faster                                                                                                    |
| pyflate                  | 293 ms                                                                                                               | 258 ms: 1.14x faster                                                                                                     |
| pickle_pure_python       | 186 us                                                                                                               | 174 us: 1.07x faster                                                                                                     |
| pprint_safe_repr         | 496 ms                                                                                                               | 466 ms: 1.06x faster                                                                                                     |
| pprint_pformat           | 1.01 sec                                                                                                             | 952 ms: 1.06x faster                                                                                                     |
| xml_etree_generate       | 55.0 ms                                                                                                              | 51.8 ms: 1.06x faster                                                                                                    |
| xml_etree_iterparse      | 63.8 ms                                                                                                              | 60.9 ms: 1.05x faster                                                                                                    |
| telco                    | 4.69 ms                                                                                                              | 4.48 ms: 1.05x faster                                                                                                    |
| regex_dna                | 122 ms                                                                                                               | 116 ms: 1.05x faster                                                                                                     |
| unpickle_pure_python     | 133 us                                                                                                               | 127 us: 1.05x faster                                                                                                     |
| logging_silent           | 57.9 ns                                                                                                              | 56.3 ns: 1.03x faster                                                                                                    |
| comprehensions           | 10.6 us                                                                                                              | 10.3 us: 1.02x faster                                                                                                    |
| xml_etree_process        | 37.8 ms                                                                                                              | 37.1 ms: 1.02x faster                                                                                                    |
| regex_effbot             | 1.59 ms                                                                                                              | 1.57 ms: 1.02x faster                                                                                                    |
| sqlglot_parse            | 813 us                                                                                                               | 805 us: 1.01x faster                                                                                                     |
| pidigits                 | 150 ms                                                                                                               | 149 ms: 1.01x faster                                                                                                     |
| logging_simple           | 5.89 us                                                                                                              | 5.84 us: 1.01x faster                                                                                                    |
| logging_format           | 6.33 us                                                                                                              | 6.28 us: 1.01x faster                                                                                                    |
| meteor_contest           | 74.9 ms                                                                                                              | 74.7 ms: 1.00x faster                                                                                                    |
| json                     | 2.94 ms                                                                                                              | 2.96 ms: 1.01x slower                                                                                                    |
| python_startup           | 20.9 ms                                                                                                              | 21.1 ms: 1.01x slower                                                                                                    |
| coverage                 | 45.8 ms                                                                                                              | 46.4 ms: 1.01x slower                                                                                                    |
| json_loads               | 14.0 us                                                                                                              | 14.2 us: 1.01x slower                                                                                                    |
| thrift                   | 509 us                                                                                                               | 518 us: 1.02x slower                                                                                                     |
| create_gc_cycles         | 885 us                                                                                                               | 902 us: 1.02x slower                                                                                                     |
| chaos                    | 39.2 ms                                                                                                              | 40.1 ms: 1.02x slower                                                                                                    |
| coroutines               | 13.3 ms                                                                                                              | 13.6 ms: 1.03x slower                                                                                                    |
| deepcopy_reduce          | 1.76 us                                                                                                              | 1.83 us: 1.04x slower                                                                                                    |
| python_startup_no_site   | 16.7 ms                                                                                                              | 17.4 ms: 1.04x slower                                                                                                    |
| tornado_http             | 80.9 ms                                                                                                              | 84.4 ms: 1.04x slower                                                                                                    |
| html5lib                 | 36.4 ms                                                                                                              | 38.1 ms: 1.05x slower                                                                                                    |
| deepcopy                 | 170 us                                                                                                               | 180 us: 1.06x slower                                                                                                     |
| bench_mp_pool            | 65.0 ms                                                                                                              | 68.7 ms: 1.06x slower                                                                                                    |
| sqlglot_optimize         | 33.1 ms                                                                                                              | 35.1 ms: 1.06x slower                                                                                                    |
| nqueens                  | 58.2 ms                                                                                                              | 61.7 ms: 1.06x slower                                                                                                    |
| sqlglot_normalize        | 175 ms                                                                                                               | 186 ms: 1.06x slower                                                                                                     |
| docutils                 | 1.63 sec                                                                                                             | 1.74 sec: 1.07x slower                                                                                                   |
| 2to3                     | 214 ms                                                                                                               | 230 ms: 1.08x slower                                                                                                     |
| sympy_str                | 164 ms                                                                                                               | 177 ms: 1.08x slower                                                                                                     |
| richards_super           | 30.6 ms                                                                                                              | 33.2 ms: 1.08x slower                                                                                                    |
| async_generators         | 233 ms                                                                                                               | 253 ms: 1.09x slower                                                                                                     |
| sympy_sum                | 84.9 ms                                                                                                              | 92.2 ms: 1.09x slower                                                                                                    |
| generators               | 21.0 ms                                                                                                              | 22.8 ms: 1.09x slower                                                                                                    |
| richards                 | 26.9 ms                                                                                                              | 29.3 ms: 1.09x slower                                                                                                    |
| go                       | 85.7 ms                                                                                                              | 93.6 ms: 1.09x slower                                                                                                    |
| sympy_expand             | 278 ms                                                                                                               | 305 ms: 1.10x slower                                                                                                     |
| raytrace                 | 167 ms                                                                                                               | 184 ms: 1.10x slower                                                                                                     |
| typing_runtime_protocols | 102 us                                                                                                               | 112 us: 1.10x slower                                                                                                     |
| sympy_integrate          | 12.5 ms                                                                                                              | 13.9 ms: 1.11x slower                                                                                                    |
| pylint                   | 205 ms                                                                                                               | 228 ms: 1.11x slower                                                                                                     |
| pycparser                | 710 ms                                                                                                               | 792 ms: 1.12x slower                                                                                                     |
| regex_compile            | 78.5 ms                                                                                                              | 87.7 ms: 1.12x slower                                                                                                    |
| scimark_sor              | 78.4 ms                                                                                                              | 87.9 ms: 1.12x slower                                                                                                    |
| deltablue                | 1.99 ms                                                                                                              | 2.25 ms: 1.13x slower                                                                                                    |
| scimark_lu               | 59.8 ms                                                                                                              | 68.5 ms: 1.15x slower                                                                                                    |
| regex_v8                 | 17.1 ms                                                                                                              | 19.9 ms: 1.17x slower                                                                                                    |
| django_template          | 23.2 ms                                                                                                              | 27.1 ms: 1.17x slower                                                                                                    |
| genshi_text              | 15.1 ms                                                                                                              | 17.9 ms: 1.19x slower                                                                                                    |
| hexiom                   | 3.90 ms                                                                                                              | 4.64 ms: 1.19x slower                                                                                                    |
| genshi_xml               | 33.1 ms                                                                                                              | 44.2 ms: 1.33x slower                                                                                                    |
| Geometric mean           | (ref)                                                                                                                | 1.00x slower                                                                                                             |

Benchmark hidden because not significant (16): async_tree_io, xml_etree_parse, async_tree_cpu_io_mixed_tg, async_tree_io_tg, mdp, asyncio_tcp, gc_traversal, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_none, pathlib, json_dumps, sqlglot_transpile, async_tree_memoization_tg, async_tree_memoization, bench_thread_pool

# HPT report

- Reliability score: 92.12% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown