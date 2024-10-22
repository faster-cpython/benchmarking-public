# Results vs. base

- fork: brandtbucher
- ref: ujb0_project
- machine: linux-x86_64
- commit hash: 8b9b14d
- commit date: 2024-09-03
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 296 ms: 1.07x slower                                                |
| docutils       | 3.04 sec                                                              | 3.51 sec: 1.16x slower                                              |
| html5lib       | 63.4 ms                                                               | 75.0 ms: 1.18x slower                                               |
| tornado_http   | 94.7 ms                                                               | 117 ms: 1.24x slower                                                |
| Geometric mean | (ref)                                                                 | 1.16x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_websockets      | 556 ms                                                                | 559 ms: 1.01x slower                                                |
| asyncio_tcp_ssl         | 1.81 sec                                                              | 1.82 sec: 1.01x slower                                              |
| async_generators        | 454 ms                                                                | 459 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed | 561 ms                                                                | 572 ms: 1.02x slower                                                |
| async_tree_io           | 924 ms                                                                | 953 ms: 1.03x slower                                                |
| async_tree_none_tg      | 307 ms                                                                | 317 ms: 1.03x slower                                                |
| async_tree_none         | 325 ms                                                                | 340 ms: 1.05x slower                                                |
| asyncio_tcp             | 499 ms                                                                | 529 ms: 1.06x slower                                                |
| coroutines              | 23.0 ms                                                               | 24.5 ms: 1.06x slower                                               |
| async_tree_memoization  | 395 ms                                                                | 426 ms: 1.08x slower                                                |
| Geometric mean          | (ref)                                                                 | 1.03x slower                                                        |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 70.4 ms                                                               | 69.1 ms: 1.02x faster                                               |
| nbody          | 82.0 ms                                                               | 80.7 ms: 1.02x faster                                               |
| pidigits       | 187 ms                                                                | 185 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 142 ms                                                                | 155 ms: 1.09x slower                                                |
| regex_dna      | 210 ms                                                                | 230 ms: 1.10x slower                                                |
| regex_effbot   | 3.51 ms                                                               | 3.87 ms: 1.10x slower                                               |
| regex_v8       | 23.9 ms                                                               | 26.4 ms: 1.11x slower                                               |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 213 us                                                                | 197 us: 1.08x faster                                                |
| xml_etree_process    | 54.7 ms                                                               | 54.2 ms: 1.01x faster                                               |
| xml_etree_iterparse  | 97.7 ms                                                               | 98.5 ms: 1.01x slower                                               |
| xml_etree_generate   | 77.7 ms                                                               | 78.4 ms: 1.01x slower                                               |
| json_loads           | 28.6 us                                                               | 29.6 us: 1.03x slower                                               |
| pickle_pure_python   | 302 us                                                                | 314 us: 1.04x slower                                                |
| tomli_loads          | 1.92 sec                                                              | 2.15 sec: 1.12x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                        |

Benchmark hidden because not significant (2): xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                               | 7.15 ms: 1.00x slower                                               |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 25.7 ms                                                               | 22.8 ms: 1.13x faster                                               |
| genshi_xml      | 59.0 ms                                                               | 60.8 ms: 1.03x slower                                               |
| django_template | 35.6 ms                                                               | 39.7 ms: 1.12x slower                                               |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                        |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text              | 25.7 ms                                                               | 22.8 ms: 1.13x faster                                               |
| unpickle_pure_python     | 213 us                                                                | 197 us: 1.08x faster                                                |
| scimark_monte_carlo      | 62.5 ms                                                               | 58.2 ms: 1.07x faster                                               |
| logging_silent           | 103 ns                                                                | 99.8 ns: 1.03x faster                                               |
| deepcopy_memo            | 27.0 us                                                               | 26.1 us: 1.03x faster                                               |
| nqueens                  | 85.7 ms                                                               | 83.5 ms: 1.03x faster                                               |
| typing_runtime_protocols | 165 us                                                                | 161 us: 1.03x faster                                                |
| float                    | 70.4 ms                                                               | 69.1 ms: 1.02x faster                                               |
| deepcopy                 | 265 us                                                                | 261 us: 1.02x faster                                                |
| nbody                    | 82.0 ms                                                               | 80.7 ms: 1.02x faster                                               |
| json                     | 5.32 ms                                                               | 5.25 ms: 1.01x faster                                               |
| fannkuch                 | 372 ms                                                                | 367 ms: 1.01x faster                                                |
| pathlib                  | 15.8 ms                                                               | 15.6 ms: 1.01x faster                                               |
| pidigits                 | 187 ms                                                                | 185 ms: 1.01x faster                                                |
| crypto_pyaes             | 66.6 ms                                                               | 65.9 ms: 1.01x faster                                               |
| xml_etree_process        | 54.7 ms                                                               | 54.2 ms: 1.01x faster                                               |
| python_startup_no_site   | 7.14 ms                                                               | 7.15 ms: 1.00x slower                                               |
| meteor_contest           | 106 ms                                                                | 107 ms: 1.00x slower                                                |
| asyncio_websockets       | 556 ms                                                                | 559 ms: 1.01x slower                                                |
| gc_traversal             | 3.58 ms                                                               | 3.60 ms: 1.01x slower                                               |
| python_startup           | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                               |
| xml_etree_iterparse      | 97.7 ms                                                               | 98.5 ms: 1.01x slower                                               |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.82 sec: 1.01x slower                                              |
| xml_etree_generate       | 77.7 ms                                                               | 78.4 ms: 1.01x slower                                               |
| scimark_sparse_mat_mult  | 4.47 ms                                                               | 4.52 ms: 1.01x slower                                               |
| coverage                 | 85.6 ms                                                               | 86.6 ms: 1.01x slower                                               |
| async_generators         | 454 ms                                                                | 459 ms: 1.01x slower                                                |
| scimark_lu               | 109 ms                                                                | 110 ms: 1.01x slower                                                |
| chaos                    | 58.6 ms                                                               | 59.4 ms: 1.01x slower                                               |
| bpe_tokeniser            | 4.43 sec                                                              | 4.52 sec: 1.02x slower                                              |
| async_tree_cpu_io_mixed  | 561 ms                                                                | 572 ms: 1.02x slower                                                |
| pprint_safe_repr         | 728 ms                                                                | 743 ms: 1.02x slower                                                |
| pyflate                  | 450 ms                                                                | 461 ms: 1.02x slower                                                |
| create_gc_cycles         | 1.75 ms                                                               | 1.79 ms: 1.02x slower                                               |
| raytrace                 | 276 ms                                                                | 284 ms: 1.03x slower                                                |
| pprint_pformat           | 1.49 sec                                                              | 1.54 sec: 1.03x slower                                              |
| genshi_xml               | 59.0 ms                                                               | 60.8 ms: 1.03x slower                                               |
| async_tree_io            | 924 ms                                                                | 953 ms: 1.03x slower                                                |
| async_tree_none_tg       | 307 ms                                                                | 317 ms: 1.03x slower                                                |
| json_loads               | 28.6 us                                                               | 29.6 us: 1.03x slower                                               |
| deepcopy_reduce          | 2.70 us                                                               | 2.79 us: 1.04x slower                                               |
| pickle_pure_python       | 302 us                                                                | 314 us: 1.04x slower                                                |
| generators               | 33.3 ms                                                               | 34.6 ms: 1.04x slower                                               |
| bench_mp_pool            | 24.0 ms                                                               | 25.0 ms: 1.04x slower                                               |
| async_tree_none          | 325 ms                                                                | 340 ms: 1.05x slower                                                |
| thrift                   | 789 us                                                                | 827 us: 1.05x slower                                                |
| go                       | 170 ms                                                                | 179 ms: 1.05x slower                                                |
| asyncio_tcp              | 499 ms                                                                | 529 ms: 1.06x slower                                                |
| coroutines               | 23.0 ms                                                               | 24.5 ms: 1.06x slower                                               |
| telco                    | 7.63 ms                                                               | 8.13 ms: 1.07x slower                                               |
| mdp                      | 2.56 sec                                                              | 2.73 sec: 1.07x slower                                              |
| 2to3                     | 276 ms                                                                | 296 ms: 1.07x slower                                                |
| scimark_sor              | 116 ms                                                                | 124 ms: 1.07x slower                                                |
| logging_simple           | 5.54 us                                                               | 5.95 us: 1.07x slower                                               |
| hexiom                   | 6.89 ms                                                               | 7.42 ms: 1.08x slower                                               |
| async_tree_memoization   | 395 ms                                                                | 426 ms: 1.08x slower                                                |
| regex_compile            | 142 ms                                                                | 155 ms: 1.09x slower                                                |
| bench_thread_pool        | 817 us                                                                | 894 us: 1.09x slower                                                |
| regex_dna                | 210 ms                                                                | 230 ms: 1.10x slower                                                |
| regex_effbot             | 3.51 ms                                                               | 3.87 ms: 1.10x slower                                               |
| regex_v8                 | 23.9 ms                                                               | 26.4 ms: 1.11x slower                                               |
| logging_format           | 6.04 us                                                               | 6.68 us: 1.11x slower                                               |
| sqlglot_normalize        | 113 ms                                                                | 125 ms: 1.11x slower                                                |
| deltablue                | 3.18 ms                                                               | 3.53 ms: 1.11x slower                                               |
| sympy_expand             | 504 ms                                                                | 559 ms: 1.11x slower                                                |
| django_template          | 35.6 ms                                                               | 39.7 ms: 1.12x slower                                               |
| tomli_loads              | 1.92 sec                                                              | 2.15 sec: 1.12x slower                                              |
| pycparser                | 1.18 sec                                                              | 1.33 sec: 1.13x slower                                              |
| richards                 | 38.6 ms                                                               | 43.9 ms: 1.14x slower                                               |
| sympy_str                | 299 ms                                                                | 344 ms: 1.15x slower                                                |
| sqlglot_optimize         | 58.1 ms                                                               | 67.1 ms: 1.15x slower                                               |
| docutils                 | 3.04 sec                                                              | 3.51 sec: 1.16x slower                                              |
| richards_super           | 45.0 ms                                                               | 52.5 ms: 1.17x slower                                               |
| html5lib                 | 63.4 ms                                                               | 75.0 ms: 1.18x slower                                               |
| sympy_integrate          | 22.8 ms                                                               | 27.4 ms: 1.20x slower                                               |
| tornado_http             | 94.7 ms                                                               | 117 ms: 1.24x slower                                                |
| sympy_sum                | 171 ms                                                                | 217 ms: 1.27x slower                                                |
| sqlglot_transpile        | 1.69 ms                                                               | 2.17 ms: 1.29x slower                                               |
| sqlglot_parse            | 1.34 ms                                                               | 1.72 ms: 1.29x slower                                               |
| pylint                   | 372 ms                                                                | 480 ms: 1.29x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.05x slower                                                        |

Benchmark hidden because not significant (9): scimark_fft, xml_etree_parse, json_dumps, async_tree_io_tg, spectral_norm, comprehensions, mako, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.11x