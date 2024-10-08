# Results vs. base

- fork: brandtbucher
- ref: ujb0_project_warmup
- machine: linux-x86_64
- commit hash: f67fedc
- commit date: 2024-09-09
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 292 ms: 1.06x slower                                                       |
| docutils       | 3.04 sec                                                              | 3.47 sec: 1.14x slower                                                     |
| html5lib       | 63.4 ms                                                               | 70.6 ms: 1.11x slower                                                      |
| tornado_http   | 94.7 ms                                                               | 119 ms: 1.26x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.14x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp_ssl         | 1.81 sec                                                              | 1.82 sec: 1.01x slower                                                     |
| async_tree_cpu_io_mixed | 561 ms                                                                | 571 ms: 1.02x slower                                                       |
| async_tree_io           | 924 ms                                                                | 947 ms: 1.03x slower                                                       |
| async_tree_none_tg      | 307 ms                                                                | 318 ms: 1.03x slower                                                       |
| async_tree_io_tg        | 886 ms                                                                | 919 ms: 1.04x slower                                                       |
| coroutines              | 23.0 ms                                                               | 23.9 ms: 1.04x slower                                                      |
| async_tree_none         | 325 ms                                                                | 339 ms: 1.04x slower                                                       |
| asyncio_tcp             | 499 ms                                                                | 522 ms: 1.05x slower                                                       |
| async_tree_memoization  | 395 ms                                                                | 422 ms: 1.07x slower                                                       |
| Geometric mean          | (ref)                                                                 | 1.03x slower                                                               |

Benchmark hidden because not significant (4): asyncio_websockets, async_generators, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 186 ms: 1.01x faster                                                       |
| float          | 70.4 ms                                                               | 69.9 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 210 ms                                                                | 215 ms: 1.02x slower                                                       |
| regex_effbot   | 3.51 ms                                                               | 3.77 ms: 1.07x slower                                                      |
| regex_v8       | 23.9 ms                                                               | 25.9 ms: 1.08x slower                                                      |
| regex_compile  | 142 ms                                                                | 155 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 213 us                                                                | 191 us: 1.11x faster                                                       |
| xml_etree_parse      | 146 ms                                                                | 144 ms: 1.01x faster                                                       |
| xml_etree_process    | 54.7 ms                                                               | 54.0 ms: 1.01x faster                                                      |
| json_dumps           | 9.98 ms                                                               | 9.90 ms: 1.01x faster                                                      |
| xml_etree_generate   | 77.7 ms                                                               | 78.1 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 97.7 ms                                                               | 98.2 ms: 1.01x slower                                                      |
| json_loads           | 28.6 us                                                               | 29.5 us: 1.03x slower                                                      |
| pickle_pure_python   | 302 us                                                                | 314 us: 1.04x slower                                                       |
| tomli_loads          | 1.92 sec                                                              | 2.06 sec: 1.07x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                               | 7.19 ms: 1.01x slower                                                      |
| python_startup         | 10.5 ms                                                               | 10.8 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 25.7 ms                                                               | 22.6 ms: 1.13x faster                                                      |
| mako            | 9.79 ms                                                               | 9.65 ms: 1.01x faster                                                      |
| django_template | 35.6 ms                                                               | 38.8 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text             | 25.7 ms                                                               | 22.6 ms: 1.13x faster                                                      |
| unpickle_pure_python    | 213 us                                                                | 191 us: 1.11x faster                                                       |
| scimark_monte_carlo     | 62.5 ms                                                               | 58.1 ms: 1.08x faster                                                      |
| scimark_sparse_mat_mult | 4.47 ms                                                               | 4.38 ms: 1.02x faster                                                      |
| nqueens                 | 85.7 ms                                                               | 84.0 ms: 1.02x faster                                                      |
| xml_etree_parse         | 146 ms                                                                | 144 ms: 1.01x faster                                                       |
| mako                    | 9.79 ms                                                               | 9.65 ms: 1.01x faster                                                      |
| xml_etree_process       | 54.7 ms                                                               | 54.0 ms: 1.01x faster                                                      |
| pidigits                | 187 ms                                                                | 186 ms: 1.01x faster                                                       |
| json_dumps              | 9.98 ms                                                               | 9.90 ms: 1.01x faster                                                      |
| float                   | 70.4 ms                                                               | 69.9 ms: 1.01x faster                                                      |
| scimark_fft             | 314 ms                                                                | 312 ms: 1.01x faster                                                       |
| xml_etree_generate      | 77.7 ms                                                               | 78.1 ms: 1.01x slower                                                      |
| xml_etree_iterparse     | 97.7 ms                                                               | 98.2 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl         | 1.81 sec                                                              | 1.82 sec: 1.01x slower                                                     |
| python_startup_no_site  | 7.14 ms                                                               | 7.19 ms: 1.01x slower                                                      |
| pathlib                 | 15.8 ms                                                               | 15.9 ms: 1.01x slower                                                      |
| comprehensions          | 16.7 us                                                               | 17.0 us: 1.02x slower                                                      |
| telco                   | 7.63 ms                                                               | 7.75 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed | 561 ms                                                                | 571 ms: 1.02x slower                                                       |
| bpe_tokeniser           | 4.43 sec                                                              | 4.51 sec: 1.02x slower                                                     |
| meteor_contest          | 106 ms                                                                | 108 ms: 1.02x slower                                                       |
| create_gc_cycles        | 1.75 ms                                                               | 1.79 ms: 1.02x slower                                                      |
| python_startup          | 10.5 ms                                                               | 10.8 ms: 1.02x slower                                                      |
| crypto_pyaes            | 66.6 ms                                                               | 68.2 ms: 1.02x slower                                                      |
| regex_dna               | 210 ms                                                                | 215 ms: 1.02x slower                                                       |
| async_tree_io           | 924 ms                                                                | 947 ms: 1.03x slower                                                       |
| thrift                  | 789 us                                                                | 809 us: 1.03x slower                                                       |
| deltablue               | 3.18 ms                                                               | 3.29 ms: 1.03x slower                                                      |
| json_loads              | 28.6 us                                                               | 29.5 us: 1.03x slower                                                      |
| deepcopy_reduce         | 2.70 us                                                               | 2.79 us: 1.03x slower                                                      |
| async_tree_none_tg      | 307 ms                                                                | 318 ms: 1.03x slower                                                       |
| hexiom                  | 6.89 ms                                                               | 7.14 ms: 1.04x slower                                                      |
| async_tree_io_tg        | 886 ms                                                                | 919 ms: 1.04x slower                                                       |
| coroutines              | 23.0 ms                                                               | 23.9 ms: 1.04x slower                                                      |
| pickle_pure_python      | 302 us                                                                | 314 us: 1.04x slower                                                       |
| go                      | 170 ms                                                                | 178 ms: 1.04x slower                                                       |
| async_tree_none         | 325 ms                                                                | 339 ms: 1.04x slower                                                       |
| generators              | 33.3 ms                                                               | 34.8 ms: 1.04x slower                                                      |
| pprint_safe_repr        | 728 ms                                                                | 761 ms: 1.05x slower                                                       |
| pyflate                 | 450 ms                                                                | 471 ms: 1.05x slower                                                       |
| asyncio_tcp             | 499 ms                                                                | 522 ms: 1.05x slower                                                       |
| scimark_sor             | 116 ms                                                                | 122 ms: 1.05x slower                                                       |
| gc_traversal            | 3.58 ms                                                               | 3.78 ms: 1.05x slower                                                      |
| 2to3                    | 276 ms                                                                | 292 ms: 1.06x slower                                                       |
| spectral_norm           | 101 ms                                                                | 107 ms: 1.06x slower                                                       |
| logging_simple          | 5.54 us                                                               | 5.88 us: 1.06x slower                                                      |
| mdp                     | 2.56 sec                                                              | 2.72 sec: 1.06x slower                                                     |
| chaos                   | 58.6 ms                                                               | 62.3 ms: 1.06x slower                                                      |
| logging_format          | 6.04 us                                                               | 6.43 us: 1.07x slower                                                      |
| async_tree_memoization  | 395 ms                                                                | 422 ms: 1.07x slower                                                       |
| tomli_loads             | 1.92 sec                                                              | 2.06 sec: 1.07x slower                                                     |
| regex_effbot            | 3.51 ms                                                               | 3.77 ms: 1.07x slower                                                      |
| regex_v8                | 23.9 ms                                                               | 25.9 ms: 1.08x slower                                                      |
| regex_compile           | 142 ms                                                                | 155 ms: 1.09x slower                                                       |
| django_template         | 35.6 ms                                                               | 38.8 ms: 1.09x slower                                                      |
| bench_thread_pool       | 817 us                                                                | 898 us: 1.10x slower                                                       |
| sqlglot_normalize       | 113 ms                                                                | 125 ms: 1.10x slower                                                       |
| sympy_expand            | 504 ms                                                                | 556 ms: 1.10x slower                                                       |
| pycparser               | 1.18 sec                                                              | 1.30 sec: 1.11x slower                                                     |
| html5lib                | 63.4 ms                                                               | 70.6 ms: 1.11x slower                                                      |
| pprint_pformat          | 1.49 sec                                                              | 1.66 sec: 1.11x slower                                                     |
| sympy_str               | 299 ms                                                                | 341 ms: 1.14x slower                                                       |
| docutils                | 3.04 sec                                                              | 3.47 sec: 1.14x slower                                                     |
| sqlglot_optimize        | 58.1 ms                                                               | 67.1 ms: 1.15x slower                                                      |
| sympy_integrate         | 22.8 ms                                                               | 27.3 ms: 1.20x slower                                                      |
| sympy_sum               | 171 ms                                                                | 214 ms: 1.25x slower                                                       |
| tornado_http            | 94.7 ms                                                               | 119 ms: 1.26x slower                                                       |
| sqlglot_transpile       | 1.69 ms                                                               | 2.17 ms: 1.29x slower                                                      |
| pylint                  | 372 ms                                                                | 480 ms: 1.29x slower                                                       |
| sqlglot_parse           | 1.34 ms                                                               | 1.73 ms: 1.29x slower                                                      |
| richards_super          | 45.0 ms                                                               | 60.8 ms: 1.35x slower                                                      |
| richards                | 38.6 ms                                                               | 53.8 ms: 1.39x slower                                                      |
| Geometric mean          | (ref)                                                                 | 1.05x slower                                                               |

Benchmark hidden because not significant (16): typing_runtime_protocols, json, raytrace, coverage, logging_silent, genshi_xml, fannkuch, asyncio_websockets, bench_mp_pool, async_generators, nbody, scimark_lu, deepcopy_memo, deepcopy, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg
Ignored benchmarks (7) of results/bm-20240909-3.14.0a0-f67fedc-JIT/bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc.json: pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.07x