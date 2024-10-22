# Results vs. base

- fork: brandtbucher
- ref: ujb0_project_warmup
- machine: linux-x86_64
- commit hash: c66bd3e
- commit date: 2024-09-09
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 292 ms: 1.06x slower                                                       |
| docutils       | 3.04 sec                                                              | 3.46 sec: 1.14x slower                                                     |
| html5lib       | 63.4 ms                                                               | 73.0 ms: 1.15x slower                                                      |
| tornado_http   | 94.7 ms                                                               | 119 ms: 1.25x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.15x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp_ssl         | 1.81 sec                                                              | 1.82 sec: 1.01x slower                                                     |
| async_tree_cpu_io_mixed | 561 ms                                                                | 573 ms: 1.02x slower                                                       |
| async_tree_io           | 924 ms                                                                | 951 ms: 1.03x slower                                                       |
| async_tree_none         | 325 ms                                                                | 338 ms: 1.04x slower                                                       |
| async_tree_none_tg      | 307 ms                                                                | 321 ms: 1.04x slower                                                       |
| asyncio_tcp             | 499 ms                                                                | 520 ms: 1.04x slower                                                       |
| coroutines              | 23.0 ms                                                               | 24.7 ms: 1.07x slower                                                      |
| async_tree_memoization  | 395 ms                                                                | 426 ms: 1.08x slower                                                       |
| Geometric mean          | (ref)                                                                 | 1.03x slower                                                               |

Benchmark hidden because not significant (5): async_generators, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 70.4 ms                                                               | 69.8 ms: 1.01x faster                                                      |
| pidigits       | 187 ms                                                                | 186 ms: 1.01x faster                                                       |
| nbody          | 82.0 ms                                                               | 83.1 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                               | 3.45 ms: 1.02x faster                                                      |
| regex_dna      | 210 ms                                                                | 206 ms: 1.02x faster                                                       |
| regex_v8       | 23.9 ms                                                               | 25.3 ms: 1.06x slower                                                      |
| regex_compile  | 142 ms                                                                | 151 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 213 us                                                                | 199 us: 1.07x faster                                                       |
| json_dumps           | 9.98 ms                                                               | 9.69 ms: 1.03x faster                                                      |
| xml_etree_process    | 54.7 ms                                                               | 53.9 ms: 1.01x faster                                                      |
| xml_etree_parse      | 146 ms                                                                | 145 ms: 1.01x faster                                                       |
| xml_etree_generate   | 77.7 ms                                                               | 78.8 ms: 1.01x slower                                                      |
| json_loads           | 28.6 us                                                               | 29.5 us: 1.03x slower                                                      |
| pickle_pure_python   | 302 us                                                                | 313 us: 1.04x slower                                                       |
| tomli_loads          | 1.92 sec                                                              | 2.07 sec: 1.08x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                               | 7.17 ms: 1.00x slower                                                      |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 25.7 ms                                                               | 22.6 ms: 1.14x faster                                                      |
| genshi_xml      | 59.0 ms                                                               | 60.0 ms: 1.02x slower                                                      |
| django_template | 35.6 ms                                                               | 40.4 ms: 1.14x slower                                                      |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text              | 25.7 ms                                                               | 22.6 ms: 1.14x faster                                                      |
| unpickle_pure_python     | 213 us                                                                | 199 us: 1.07x faster                                                       |
| scimark_monte_carlo      | 62.5 ms                                                               | 58.4 ms: 1.07x faster                                                      |
| scimark_sparse_mat_mult  | 4.47 ms                                                               | 4.20 ms: 1.06x faster                                                      |
| typing_runtime_protocols | 165 us                                                                | 159 us: 1.04x faster                                                       |
| json_dumps               | 9.98 ms                                                               | 9.69 ms: 1.03x faster                                                      |
| scimark_fft              | 314 ms                                                                | 307 ms: 1.02x faster                                                       |
| pyflate                  | 450 ms                                                                | 441 ms: 1.02x faster                                                       |
| nqueens                  | 85.7 ms                                                               | 84.1 ms: 1.02x faster                                                      |
| crypto_pyaes             | 66.6 ms                                                               | 65.4 ms: 1.02x faster                                                      |
| regex_effbot             | 3.51 ms                                                               | 3.45 ms: 1.02x faster                                                      |
| regex_dna                | 210 ms                                                                | 206 ms: 1.02x faster                                                       |
| xml_etree_process        | 54.7 ms                                                               | 53.9 ms: 1.01x faster                                                      |
| xml_etree_parse          | 146 ms                                                                | 145 ms: 1.01x faster                                                       |
| comprehensions           | 16.7 us                                                               | 16.5 us: 1.01x faster                                                      |
| deepcopy_memo            | 27.0 us                                                               | 26.7 us: 1.01x faster                                                      |
| float                    | 70.4 ms                                                               | 69.8 ms: 1.01x faster                                                      |
| pidigits                 | 187 ms                                                                | 186 ms: 1.01x faster                                                       |
| mdp                      | 2.56 sec                                                              | 2.54 sec: 1.01x faster                                                     |
| python_startup_no_site   | 7.14 ms                                                               | 7.17 ms: 1.00x slower                                                      |
| spectral_norm            | 101 ms                                                                | 102 ms: 1.01x slower                                                       |
| bench_mp_pool            | 24.0 ms                                                               | 24.2 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.82 sec: 1.01x slower                                                     |
| thrift                   | 789 us                                                                | 795 us: 1.01x slower                                                       |
| deepcopy                 | 265 us                                                                | 268 us: 1.01x slower                                                       |
| python_startup           | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                      |
| nbody                    | 82.0 ms                                                               | 83.1 ms: 1.01x slower                                                      |
| meteor_contest           | 106 ms                                                                | 108 ms: 1.01x slower                                                       |
| xml_etree_generate       | 77.7 ms                                                               | 78.8 ms: 1.01x slower                                                      |
| genshi_xml               | 59.0 ms                                                               | 60.0 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed  | 561 ms                                                                | 573 ms: 1.02x slower                                                       |
| bpe_tokeniser            | 4.43 sec                                                              | 4.54 sec: 1.03x slower                                                     |
| async_tree_io            | 924 ms                                                                | 951 ms: 1.03x slower                                                       |
| generators               | 33.3 ms                                                               | 34.3 ms: 1.03x slower                                                      |
| json_loads               | 28.6 us                                                               | 29.5 us: 1.03x slower                                                      |
| telco                    | 7.63 ms                                                               | 7.88 ms: 1.03x slower                                                      |
| pprint_safe_repr         | 728 ms                                                                | 753 ms: 1.03x slower                                                       |
| create_gc_cycles         | 1.75 ms                                                               | 1.81 ms: 1.03x slower                                                      |
| pickle_pure_python       | 302 us                                                                | 313 us: 1.04x slower                                                       |
| async_tree_none          | 325 ms                                                                | 338 ms: 1.04x slower                                                       |
| pprint_pformat           | 1.49 sec                                                              | 1.56 sec: 1.04x slower                                                     |
| async_tree_none_tg       | 307 ms                                                                | 321 ms: 1.04x slower                                                       |
| asyncio_tcp              | 499 ms                                                                | 520 ms: 1.04x slower                                                       |
| raytrace                 | 276 ms                                                                | 289 ms: 1.05x slower                                                       |
| go                       | 170 ms                                                                | 178 ms: 1.05x slower                                                       |
| gc_traversal             | 3.58 ms                                                               | 3.76 ms: 1.05x slower                                                      |
| hexiom                   | 6.89 ms                                                               | 7.27 ms: 1.06x slower                                                      |
| 2to3                     | 276 ms                                                                | 292 ms: 1.06x slower                                                       |
| richards                 | 38.6 ms                                                               | 40.9 ms: 1.06x slower                                                      |
| regex_v8                 | 23.9 ms                                                               | 25.3 ms: 1.06x slower                                                      |
| logging_simple           | 5.54 us                                                               | 5.88 us: 1.06x slower                                                      |
| regex_compile            | 142 ms                                                                | 151 ms: 1.06x slower                                                       |
| coroutines               | 23.0 ms                                                               | 24.7 ms: 1.07x slower                                                      |
| scimark_sor              | 116 ms                                                                | 124 ms: 1.07x slower                                                       |
| logging_silent           | 103 ns                                                                | 111 ns: 1.07x slower                                                       |
| tomli_loads              | 1.92 sec                                                              | 2.07 sec: 1.08x slower                                                     |
| async_tree_memoization   | 395 ms                                                                | 426 ms: 1.08x slower                                                       |
| bench_thread_pool        | 817 us                                                                | 895 us: 1.10x slower                                                       |
| sympy_expand             | 504 ms                                                                | 557 ms: 1.10x slower                                                       |
| sqlglot_normalize        | 113 ms                                                                | 126 ms: 1.11x slower                                                       |
| logging_format           | 6.04 us                                                               | 6.74 us: 1.12x slower                                                      |
| deltablue                | 3.18 ms                                                               | 3.57 ms: 1.12x slower                                                      |
| django_template          | 35.6 ms                                                               | 40.4 ms: 1.14x slower                                                      |
| pycparser                | 1.18 sec                                                              | 1.34 sec: 1.14x slower                                                     |
| docutils                 | 3.04 sec                                                              | 3.46 sec: 1.14x slower                                                     |
| richards_super           | 45.0 ms                                                               | 51.4 ms: 1.14x slower                                                      |
| sympy_str                | 299 ms                                                                | 341 ms: 1.14x slower                                                       |
| html5lib                 | 63.4 ms                                                               | 73.0 ms: 1.15x slower                                                      |
| sqlglot_optimize         | 58.1 ms                                                               | 67.8 ms: 1.17x slower                                                      |
| sympy_integrate          | 22.8 ms                                                               | 27.6 ms: 1.21x slower                                                      |
| tornado_http             | 94.7 ms                                                               | 119 ms: 1.25x slower                                                       |
| sympy_sum                | 171 ms                                                                | 215 ms: 1.26x slower                                                       |
| sqlglot_parse            | 1.34 ms                                                               | 1.69 ms: 1.27x slower                                                      |
| sqlglot_transpile        | 1.69 ms                                                               | 2.15 ms: 1.27x slower                                                      |
| pylint                   | 372 ms                                                                | 482 ms: 1.29x slower                                                       |
| Geometric mean           | (ref)                                                                 | 1.04x slower                                                               |

Benchmark hidden because not significant (14): json, deepcopy_reduce, pathlib, mako, scimark_lu, async_generators, xml_etree_iterparse, asyncio_websockets, chaos, coverage, fannkuch, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg
Ignored benchmarks (7) of results/bm-20240909-3.14.0a0-c66bd3e-JIT/bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e.json: pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.09x