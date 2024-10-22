# Results vs. base

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-x86_64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.02x slower
- HPT reliability: 86.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 284 ms                                                                                                                | 314 ms: 1.11x slower                                                                                                      |
| docutils       | 2.98 sec                                                                                                              | 3.28 sec: 1.10x slower                                                                                                    |
| html5lib       | 73.6 ms                                                                                                               | 72.4 ms: 1.02x faster                                                                                                     |
| tornado_http   | 116 ms                                                                                                                | 122 ms: 1.05x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.06x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|-------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none         | 336 ms                                                                                                                | 321 ms: 1.05x faster                                                                                                      |
| async_tree_cpu_io_mixed | 577 ms                                                                                                                | 560 ms: 1.03x faster                                                                                                      |
| asyncio_tcp_ssl         | 1.58 sec                                                                                                              | 1.58 sec: 1.00x slower                                                                                                    |
| coroutines              | 21.2 ms                                                                                                               | 21.5 ms: 1.01x slower                                                                                                     |
| asyncio_websockets      | 389 ms                                                                                                                | 396 ms: 1.02x slower                                                                                                      |
| asyncio_tcp             | 372 ms                                                                                                                | 378 ms: 1.02x slower                                                                                                      |
| async_tree_io           | 800 ms                                                                                                                | 819 ms: 1.02x slower                                                                                                      |
| async_tree_memoization  | 401 ms                                                                                                                | 412 ms: 1.03x slower                                                                                                      |
| async_generators        | 364 ms                                                                                                                | 382 ms: 1.05x slower                                                                                                      |
| Geometric mean          | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 79.6 ms                                                                                                               | 75.0 ms: 1.06x faster                                                                                                     |
| nbody          | 86.3 ms                                                                                                               | 83.3 ms: 1.04x faster                                                                                                     |
| pidigits       | 253 ms                                                                                                                | 250 ms: 1.01x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.04x faster                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.59 ms                                                                                                               | 3.67 ms: 1.02x slower                                                                                                     |
| regex_v8       | 25.8 ms                                                                                                               | 26.9 ms: 1.04x slower                                                                                                     |
| regex_compile  | 139 ms                                                                                                                | 145 ms: 1.05x slower                                                                                                      |
| regex_dna      | 240 ms                                                                                                                | 261 ms: 1.09x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.05x slower                                                                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_generate   | 84.7 ms                                                                                                               | 77.7 ms: 1.09x faster                                                                                                     |
| tomli_loads          | 2.27 sec                                                                                                              | 2.12 sec: 1.07x faster                                                                                                    |
| xml_etree_process    | 58.7 ms                                                                                                               | 55.3 ms: 1.06x faster                                                                                                     |
| xml_etree_iterparse  | 101 ms                                                                                                                | 98.0 ms: 1.03x faster                                                                                                     |
| json_dumps           | 10.7 ms                                                                                                               | 10.4 ms: 1.02x faster                                                                                                     |
| xml_etree_parse      | 143 ms                                                                                                                | 141 ms: 1.01x faster                                                                                                      |
| unpickle_pure_python | 214 us                                                                                                                | 213 us: 1.01x faster                                                                                                      |
| pickle_pure_python   | 312 us                                                                                                                | 319 us: 1.02x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                 | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| mako            | 10.5 ms                                                                                                               | 9.16 ms: 1.14x faster                                                                                                     |
| django_template | 38.9 ms                                                                                                               | 42.1 ms: 1.08x slower                                                                                                     |
| genshi_xml      | 55.0 ms                                                                                                               | 64.5 ms: 1.17x slower                                                                                                     |
| genshi_text     | 25.4 ms                                                                                                               | 30.3 ms: 1.20x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                                 | 1.07x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|--------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| spectral_norm            | 96.6 ms                                                                                                               | 82.1 ms: 1.18x faster                                                                                                     |
| mako                     | 10.5 ms                                                                                                               | 9.16 ms: 1.14x faster                                                                                                     |
| richards                 | 49.4 ms                                                                                                               | 43.8 ms: 1.13x faster                                                                                                     |
| richards_super           | 55.4 ms                                                                                                               | 50.7 ms: 1.09x faster                                                                                                     |
| xml_etree_generate       | 84.7 ms                                                                                                               | 77.7 ms: 1.09x faster                                                                                                     |
| scimark_sor              | 110 ms                                                                                                                | 101 ms: 1.08x faster                                                                                                      |
| deepcopy_memo            | 29.3 us                                                                                                               | 27.2 us: 1.08x faster                                                                                                     |
| tomli_loads              | 2.27 sec                                                                                                              | 2.12 sec: 1.07x faster                                                                                                    |
| deltablue                | 3.31 ms                                                                                                               | 3.11 ms: 1.07x faster                                                                                                     |
| xml_etree_process        | 58.7 ms                                                                                                               | 55.3 ms: 1.06x faster                                                                                                     |
| float                    | 79.6 ms                                                                                                               | 75.0 ms: 1.06x faster                                                                                                     |
| crypto_pyaes             | 73.1 ms                                                                                                               | 69.2 ms: 1.06x faster                                                                                                     |
| scimark_sparse_mat_mult  | 4.22 ms                                                                                                               | 4.00 ms: 1.06x faster                                                                                                     |
| scimark_fft              | 299 ms                                                                                                                | 285 ms: 1.05x faster                                                                                                      |
| async_tree_none          | 336 ms                                                                                                                | 321 ms: 1.05x faster                                                                                                      |
| nbody                    | 86.3 ms                                                                                                               | 83.3 ms: 1.04x faster                                                                                                     |
| async_tree_cpu_io_mixed  | 577 ms                                                                                                                | 560 ms: 1.03x faster                                                                                                      |
| bpe_tokeniser            | 5.01 sec                                                                                                              | 4.87 sec: 1.03x faster                                                                                                    |
| xml_etree_iterparse      | 101 ms                                                                                                                | 98.0 ms: 1.03x faster                                                                                                     |
| gc_traversal             | 4.48 ms                                                                                                               | 4.37 ms: 1.03x faster                                                                                                     |
| create_gc_cycles         | 1.97 ms                                                                                                               | 1.93 ms: 1.02x faster                                                                                                     |
| json_dumps               | 10.7 ms                                                                                                               | 10.4 ms: 1.02x faster                                                                                                     |
| telco                    | 7.98 ms                                                                                                               | 7.85 ms: 1.02x faster                                                                                                     |
| html5lib                 | 73.6 ms                                                                                                               | 72.4 ms: 1.02x faster                                                                                                     |
| pprint_safe_repr         | 814 ms                                                                                                                | 804 ms: 1.01x faster                                                                                                      |
| xml_etree_parse          | 143 ms                                                                                                                | 141 ms: 1.01x faster                                                                                                      |
| pidigits                 | 253 ms                                                                                                                | 250 ms: 1.01x faster                                                                                                      |
| pathlib                  | 16.0 ms                                                                                                               | 15.9 ms: 1.01x faster                                                                                                     |
| pyflate                  | 478 ms                                                                                                                | 475 ms: 1.01x faster                                                                                                      |
| unpickle_pure_python     | 214 us                                                                                                                | 213 us: 1.01x faster                                                                                                      |
| asyncio_tcp_ssl          | 1.58 sec                                                                                                              | 1.58 sec: 1.00x slower                                                                                                    |
| fannkuch                 | 357 ms                                                                                                                | 360 ms: 1.01x slower                                                                                                      |
| coroutines               | 21.2 ms                                                                                                               | 21.5 ms: 1.01x slower                                                                                                     |
| scimark_lu               | 94.1 ms                                                                                                               | 95.2 ms: 1.01x slower                                                                                                     |
| deepcopy_reduce          | 2.86 us                                                                                                               | 2.91 us: 1.02x slower                                                                                                     |
| asyncio_websockets       | 389 ms                                                                                                                | 396 ms: 1.02x slower                                                                                                      |
| asyncio_tcp              | 372 ms                                                                                                                | 378 ms: 1.02x slower                                                                                                      |
| meteor_contest           | 128 ms                                                                                                                | 131 ms: 1.02x slower                                                                                                      |
| regex_effbot             | 3.59 ms                                                                                                               | 3.67 ms: 1.02x slower                                                                                                     |
| pickle_pure_python       | 312 us                                                                                                                | 319 us: 1.02x slower                                                                                                      |
| async_tree_io            | 800 ms                                                                                                                | 819 ms: 1.02x slower                                                                                                      |
| thrift                   | 877 us                                                                                                                | 898 us: 1.02x slower                                                                                                      |
| go                       | 158 ms                                                                                                                | 163 ms: 1.03x slower                                                                                                      |
| async_tree_memoization   | 401 ms                                                                                                                | 412 ms: 1.03x slower                                                                                                      |
| pycparser                | 1.21 sec                                                                                                              | 1.25 sec: 1.03x slower                                                                                                    |
| logging_silent           | 96.3 ns                                                                                                               | 99.5 ns: 1.03x slower                                                                                                     |
| logging_format           | 6.92 us                                                                                                               | 7.16 us: 1.03x slower                                                                                                     |
| mdp                      | 2.49 sec                                                                                                              | 2.58 sec: 1.04x slower                                                                                                    |
| bench_mp_pool            | 4.67 ms                                                                                                               | 4.84 ms: 1.04x slower                                                                                                     |
| logging_simple           | 6.25 us                                                                                                               | 6.49 us: 1.04x slower                                                                                                     |
| regex_v8                 | 25.8 ms                                                                                                               | 26.9 ms: 1.04x slower                                                                                                     |
| regex_compile            | 139 ms                                                                                                                | 145 ms: 1.05x slower                                                                                                      |
| async_generators         | 364 ms                                                                                                                | 382 ms: 1.05x slower                                                                                                      |
| raytrace                 | 269 ms                                                                                                                | 283 ms: 1.05x slower                                                                                                      |
| sqlglot_parse            | 1.41 ms                                                                                                               | 1.48 ms: 1.05x slower                                                                                                     |
| tornado_http             | 116 ms                                                                                                                | 122 ms: 1.05x slower                                                                                                      |
| scimark_monte_carlo      | 64.9 ms                                                                                                               | 68.4 ms: 1.05x slower                                                                                                     |
| deepcopy                 | 285 us                                                                                                                | 301 us: 1.05x slower                                                                                                      |
| comprehensions           | 17.2 us                                                                                                               | 18.3 us: 1.06x slower                                                                                                     |
| bench_thread_pool        | 865 us                                                                                                                | 920 us: 1.06x slower                                                                                                      |
| sympy_str                | 295 ms                                                                                                                | 315 ms: 1.07x slower                                                                                                      |
| sympy_expand             | 497 ms                                                                                                                | 535 ms: 1.08x slower                                                                                                      |
| typing_runtime_protocols | 174 us                                                                                                                | 188 us: 1.08x slower                                                                                                      |
| chaos                    | 61.0 ms                                                                                                               | 65.9 ms: 1.08x slower                                                                                                     |
| django_template          | 38.9 ms                                                                                                               | 42.1 ms: 1.08x slower                                                                                                     |
| regex_dna                | 240 ms                                                                                                                | 261 ms: 1.09x slower                                                                                                      |
| nqueens                  | 90.9 ms                                                                                                               | 99.0 ms: 1.09x slower                                                                                                     |
| sqlglot_normalize        | 118 ms                                                                                                                | 129 ms: 1.09x slower                                                                                                      |
| hexiom                   | 6.36 ms                                                                                                               | 6.95 ms: 1.09x slower                                                                                                     |
| sqlglot_transpile        | 1.78 ms                                                                                                               | 1.96 ms: 1.10x slower                                                                                                     |
| docutils                 | 2.98 sec                                                                                                              | 3.28 sec: 1.10x slower                                                                                                    |
| 2to3                     | 284 ms                                                                                                                | 314 ms: 1.11x slower                                                                                                      |
| sympy_sum                | 154 ms                                                                                                                | 172 ms: 1.12x slower                                                                                                      |
| sqlglot_optimize         | 58.4 ms                                                                                                               | 65.9 ms: 1.13x slower                                                                                                     |
| sympy_integrate          | 23.1 ms                                                                                                               | 26.7 ms: 1.16x slower                                                                                                     |
| pylint                   | 347 ms                                                                                                                | 405 ms: 1.17x slower                                                                                                      |
| genshi_xml               | 55.0 ms                                                                                                               | 64.5 ms: 1.17x slower                                                                                                     |
| genshi_text              | 25.4 ms                                                                                                               | 30.3 ms: 1.20x slower                                                                                                     |
| generators               | 28.4 ms                                                                                                               | 37.8 ms: 1.33x slower                                                                                                     |
| Geometric mean           | (ref)                                                                                                                 | 1.02x slower                                                                                                              |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed_tg, pprint_pformat, python_startup, python_startup_no_site, json, async_tree_io_tg, coverage, json_loads, async_tree_none_tg, async_tree_memoization_tg

# HPT report

- Reliability score: 86.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x