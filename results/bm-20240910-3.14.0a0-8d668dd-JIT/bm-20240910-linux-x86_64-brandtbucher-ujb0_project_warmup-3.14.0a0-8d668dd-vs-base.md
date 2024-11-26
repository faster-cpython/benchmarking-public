# Results vs. base

- fork: brandtbucher
- ref: ujb0_project_warmup
- machine: linux-x86_64
- commit hash: 8d668dd
- commit date: 2024-09-10
- overall geometric mean: 1.044x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 289 ms: 1.05x slower                                                       |
| docutils       | 3.04 sec                                                              | 3.48 sec: 1.15x slower                                                     |
| html5lib       | 63.4 ms                                                               | 74.4 ms: 1.17x slower                                                      |
| tornado_http   | 94.7 ms                                                               | 114 ms: 1.21x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.14x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_generators        | 454 ms                                                                | 457 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl         | 1.81 sec                                                              | 1.82 sec: 1.01x slower                                                     |
| async_tree_cpu_io_mixed | 561 ms                                                                | 571 ms: 1.02x slower                                                       |
| async_tree_none_tg      | 307 ms                                                                | 316 ms: 1.03x slower                                                       |
| async_tree_io_tg        | 886 ms                                                                | 913 ms: 1.03x slower                                                       |
| async_tree_io           | 924 ms                                                                | 953 ms: 1.03x slower                                                       |
| async_tree_none         | 325 ms                                                                | 338 ms: 1.04x slower                                                       |
| coroutines              | 23.0 ms                                                               | 24.1 ms: 1.05x slower                                                      |
| asyncio_tcp             | 499 ms                                                                | 525 ms: 1.05x slower                                                       |
| async_tree_memoization  | 395 ms                                                                | 423 ms: 1.07x slower                                                       |
| Geometric mean          | (ref)                                                                 | 1.03x slower                                                               |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 70.4 ms                                                               | 68.4 ms: 1.03x faster                                                      |
| nbody          | 82.0 ms                                                               | 79.8 ms: 1.03x faster                                                      |
| pidigits       | 187 ms                                                                | 186 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 210 ms                                                                | 219 ms: 1.04x slower                                                       |
| regex_effbot   | 3.51 ms                                                               | 3.72 ms: 1.06x slower                                                      |
| regex_compile  | 142 ms                                                                | 151 ms: 1.07x slower                                                       |
| regex_v8       | 23.9 ms                                                               | 25.8 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 213 us                                                                | 196 us: 1.08x faster                                                       |
| xml_etree_iterparse  | 97.7 ms                                                               | 98.0 ms: 1.00x slower                                                      |
| xml_etree_generate   | 77.7 ms                                                               | 78.7 ms: 1.01x slower                                                      |
| json_loads           | 28.6 us                                                               | 29.7 us: 1.04x slower                                                      |
| pickle_pure_python   | 302 us                                                                | 319 us: 1.06x slower                                                       |
| tomli_loads          | 1.92 sec                                                              | 2.13 sec: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                               |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                               | 7.15 ms: 1.00x slower                                                      |
| python_startup         | 10.5 ms                                                               | 10.7 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 25.7 ms                                                               | 23.1 ms: 1.11x faster                                                      |
| mako            | 9.79 ms                                                               | 9.86 ms: 1.01x slower                                                      |
| genshi_xml      | 59.0 ms                                                               | 62.3 ms: 1.06x slower                                                      |
| django_template | 35.6 ms                                                               | 40.4 ms: 1.14x slower                                                      |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text              | 25.7 ms                                                               | 23.1 ms: 1.11x faster                                                      |
| unpickle_pure_python     | 213 us                                                                | 196 us: 1.08x faster                                                       |
| scimark_monte_carlo      | 62.5 ms                                                               | 58.8 ms: 1.06x faster                                                      |
| scimark_sparse_mat_mult  | 4.47 ms                                                               | 4.27 ms: 1.05x faster                                                      |
| pyflate                  | 450 ms                                                                | 436 ms: 1.03x faster                                                       |
| float                    | 70.4 ms                                                               | 68.4 ms: 1.03x faster                                                      |
| nqueens                  | 85.7 ms                                                               | 83.3 ms: 1.03x faster                                                      |
| typing_runtime_protocols | 165 us                                                                | 161 us: 1.03x faster                                                       |
| nbody                    | 82.0 ms                                                               | 79.8 ms: 1.03x faster                                                      |
| logging_silent           | 103 ns                                                                | 102 ns: 1.01x faster                                                       |
| scimark_fft              | 314 ms                                                                | 310 ms: 1.01x faster                                                       |
| json                     | 5.32 ms                                                               | 5.25 ms: 1.01x faster                                                      |
| gc_traversal             | 3.58 ms                                                               | 3.55 ms: 1.01x faster                                                      |
| pidigits                 | 187 ms                                                                | 186 ms: 1.01x faster                                                       |
| python_startup_no_site   | 7.14 ms                                                               | 7.15 ms: 1.00x slower                                                      |
| xml_etree_iterparse      | 97.7 ms                                                               | 98.0 ms: 1.00x slower                                                      |
| async_generators         | 454 ms                                                                | 457 ms: 1.01x slower                                                       |
| mako                     | 9.79 ms                                                               | 9.86 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.82 sec: 1.01x slower                                                     |
| scimark_lu               | 109 ms                                                                | 110 ms: 1.01x slower                                                       |
| fannkuch                 | 372 ms                                                                | 376 ms: 1.01x slower                                                       |
| xml_etree_generate       | 77.7 ms                                                               | 78.7 ms: 1.01x slower                                                      |
| coverage                 | 85.6 ms                                                               | 86.8 ms: 1.01x slower                                                      |
| create_gc_cycles         | 1.75 ms                                                               | 1.78 ms: 1.01x slower                                                      |
| python_startup           | 10.5 ms                                                               | 10.7 ms: 1.02x slower                                                      |
| spectral_norm            | 101 ms                                                                | 103 ms: 1.02x slower                                                       |
| deepcopy_reduce          | 2.70 us                                                               | 2.74 us: 1.02x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                               | 24.4 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed  | 561 ms                                                                | 571 ms: 1.02x slower                                                       |
| raytrace                 | 276 ms                                                                | 281 ms: 1.02x slower                                                       |
| chaos                    | 58.6 ms                                                               | 59.9 ms: 1.02x slower                                                      |
| bpe_tokeniser            | 4.43 sec                                                              | 4.55 sec: 1.03x slower                                                     |
| thrift                   | 789 us                                                                | 809 us: 1.03x slower                                                       |
| scimark_sor              | 116 ms                                                                | 119 ms: 1.03x slower                                                       |
| async_tree_none_tg       | 307 ms                                                                | 316 ms: 1.03x slower                                                       |
| meteor_contest           | 106 ms                                                                | 109 ms: 1.03x slower                                                       |
| async_tree_io_tg         | 886 ms                                                                | 913 ms: 1.03x slower                                                       |
| async_tree_io            | 924 ms                                                                | 953 ms: 1.03x slower                                                       |
| go                       | 170 ms                                                                | 176 ms: 1.03x slower                                                       |
| json_loads               | 28.6 us                                                               | 29.7 us: 1.04x slower                                                      |
| async_tree_none          | 325 ms                                                                | 338 ms: 1.04x slower                                                       |
| regex_dna                | 210 ms                                                                | 219 ms: 1.04x slower                                                       |
| generators               | 33.3 ms                                                               | 34.7 ms: 1.04x slower                                                      |
| coroutines               | 23.0 ms                                                               | 24.1 ms: 1.05x slower                                                      |
| 2to3                     | 276 ms                                                                | 289 ms: 1.05x slower                                                       |
| asyncio_tcp              | 499 ms                                                                | 525 ms: 1.05x slower                                                       |
| logging_simple           | 5.54 us                                                               | 5.83 us: 1.05x slower                                                      |
| deepcopy                 | 265 us                                                                | 280 us: 1.05x slower                                                       |
| genshi_xml               | 59.0 ms                                                               | 62.3 ms: 1.06x slower                                                      |
| pickle_pure_python       | 302 us                                                                | 319 us: 1.06x slower                                                       |
| mdp                      | 2.56 sec                                                              | 2.72 sec: 1.06x slower                                                     |
| regex_effbot             | 3.51 ms                                                               | 3.72 ms: 1.06x slower                                                      |
| pprint_safe_repr         | 728 ms                                                                | 776 ms: 1.07x slower                                                       |
| regex_compile            | 142 ms                                                                | 151 ms: 1.07x slower                                                       |
| async_tree_memoization   | 395 ms                                                                | 423 ms: 1.07x slower                                                       |
| regex_v8                 | 23.9 ms                                                               | 25.8 ms: 1.08x slower                                                      |
| logging_format           | 6.04 us                                                               | 6.53 us: 1.08x slower                                                      |
| hexiom                   | 6.89 ms                                                               | 7.49 ms: 1.09x slower                                                      |
| bench_thread_pool        | 817 us                                                                | 892 us: 1.09x slower                                                       |
| sympy_expand             | 504 ms                                                                | 554 ms: 1.10x slower                                                       |
| sqlglot_optimize         | 58.1 ms                                                               | 64.0 ms: 1.10x slower                                                      |
| tomli_loads              | 1.92 sec                                                              | 2.13 sec: 1.10x slower                                                     |
| sympy_integrate          | 22.8 ms                                                               | 25.3 ms: 1.11x slower                                                      |
| pprint_pformat           | 1.49 sec                                                              | 1.66 sec: 1.11x slower                                                     |
| sqlglot_normalize        | 113 ms                                                                | 126 ms: 1.12x slower                                                       |
| sympy_str                | 299 ms                                                                | 336 ms: 1.12x slower                                                       |
| deltablue                | 3.18 ms                                                               | 3.59 ms: 1.13x slower                                                      |
| django_template          | 35.6 ms                                                               | 40.4 ms: 1.14x slower                                                      |
| pycparser                | 1.18 sec                                                              | 1.35 sec: 1.14x slower                                                     |
| docutils                 | 3.04 sec                                                              | 3.48 sec: 1.15x slower                                                     |
| html5lib                 | 63.4 ms                                                               | 74.4 ms: 1.17x slower                                                      |
| tornado_http             | 94.7 ms                                                               | 114 ms: 1.21x slower                                                       |
| sympy_sum                | 171 ms                                                                | 209 ms: 1.22x slower                                                       |
| pylint                   | 372 ms                                                                | 454 ms: 1.22x slower                                                       |
| sqlglot_transpile        | 1.69 ms                                                               | 2.08 ms: 1.24x slower                                                      |
| richards_super           | 45.0 ms                                                               | 55.8 ms: 1.24x slower                                                      |
| richards                 | 38.6 ms                                                               | 48.3 ms: 1.25x slower                                                      |
| sqlglot_parse            | 1.34 ms                                                               | 1.68 ms: 1.26x slower                                                      |
| Geometric mean           | (ref)                                                                 | 1.05x slower                                                               |

Benchmark hidden because not significant (11): xml_etree_process, xml_etree_parse, json_dumps, telco, comprehensions, pathlib, asyncio_websockets, crypto_pyaes, deepcopy_memo, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg
Ignored benchmarks (7) of results/bm-20240910-3.14.0a0-8d668dd-JIT/bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd.json: pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.044x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.07x