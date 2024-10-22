# Results vs. 3.13.0

- fork: python
- ref: 498376d7a7d6f704f22a
- machine: windows-amd64
- commit hash: 498376d
- commit date: 2024-08-02
- overall geometric mean: 1.01x faster
- HPT reliability: 97.87%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 240 ms: 1.11x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.84 sec: 1.17x slower                                                     |
| html5lib       | 38.6 ms                                                     | 41.0 ms: 1.06x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 96.1 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|---------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg | 288 ms                                                      | 246 ms: 1.17x faster                                                       |
| async_tree_none_tg        | 206 ms                                                      | 189 ms: 1.09x faster                                                       |
| asyncio_tcp_ssl           | 1.64 sec                                                    | 1.52 sec: 1.08x faster                                                     |
| async_tree_none           | 223 ms                                                      | 212 ms: 1.05x faster                                                       |
| async_tree_memoization    | 271 ms                                                      | 259 ms: 1.05x faster                                                       |
| asyncio_tcp               | 654 ms                                                      | 638 ms: 1.02x faster                                                       |
| async_tree_io_tg          | 512 ms                                                      | 537 ms: 1.05x slower                                                       |
| async_tree_io             | 521 ms                                                      | 551 ms: 1.06x slower                                                       |
| coroutines                | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| async_generators          | 223 ms                                                      | 256 ms: 1.15x slower                                                       |
| Geometric mean            | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 49.8 ms: 1.30x faster                                                      |
| float          | 48.1 ms                                                     | 44.9 ms: 1.07x faster                                                      |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 14.7 ms                                                     | 15.4 ms: 1.05x slower                                                      |
| regex_dna      | 114 ms                                                      | 122 ms: 1.06x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 89.4 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.25 sec: 1.09x faster                                                     |
| xml_etree_generate   | 53.3 ms                                                     | 52.6 ms: 1.01x faster                                                      |
| pickle_pure_python   | 183 us                                                      | 181 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 62.3 ms                                                     | 61.5 ms: 1.01x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 37.5 ms: 1.03x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 5.99 ms: 1.04x slower                                                      |
| unpickle_pure_python | 127 us                                                      | 136 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 22.0 ms: 1.01x faster                                                      |
| python_startup_no_site | 17.8 ms                                                     | 18.2 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 4.96 ms: 1.26x faster                                                      |
| django_template | 21.8 ms                                                     | 24.7 ms: 1.14x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 39.0 ms: 1.19x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.9 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|---------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.68 ms                                                     | 519 us: 16.71x faster                                                      |
| deepcopy_memo             | 21.8 us                                                     | 16.2 us: 1.35x faster                                                      |
| nbody                     | 64.5 ms                                                     | 49.8 ms: 1.30x faster                                                      |
| spectral_norm             | 59.2 ms                                                     | 46.1 ms: 1.28x faster                                                      |
| mako                      | 6.24 ms                                                     | 4.96 ms: 1.26x faster                                                      |
| deepcopy                  | 223 us                                                      | 183 us: 1.22x faster                                                       |
| scimark_sor               | 72.0 ms                                                     | 59.9 ms: 1.20x faster                                                      |
| scimark_fft               | 174 ms                                                      | 148 ms: 1.18x faster                                                       |
| async_tree_memoization_tg | 288 ms                                                      | 246 ms: 1.17x faster                                                       |
| deepcopy_reduce           | 2.02 us                                                     | 1.78 us: 1.13x faster                                                      |
| scimark_sparse_mat_mult   | 2.34 ms                                                     | 2.07 ms: 1.13x faster                                                      |
| fannkuch                  | 245 ms                                                      | 220 ms: 1.11x faster                                                       |
| tomli_loads               | 1.36 sec                                                    | 1.25 sec: 1.09x faster                                                     |
| async_tree_none_tg        | 206 ms                                                      | 189 ms: 1.09x faster                                                       |
| asyncio_tcp_ssl           | 1.64 sec                                                    | 1.52 sec: 1.08x faster                                                     |
| crypto_pyaes              | 42.8 ms                                                     | 39.9 ms: 1.07x faster                                                      |
| scimark_monte_carlo       | 40.3 ms                                                     | 37.5 ms: 1.07x faster                                                      |
| float                     | 48.1 ms                                                     | 44.9 ms: 1.07x faster                                                      |
| pyflate                   | 275 ms                                                      | 257 ms: 1.07x faster                                                       |
| telco                     | 4.85 ms                                                     | 4.54 ms: 1.07x faster                                                      |
| async_tree_none           | 223 ms                                                      | 212 ms: 1.05x faster                                                       |
| async_tree_memoization    | 271 ms                                                      | 259 ms: 1.05x faster                                                       |
| pprint_safe_repr          | 493 ms                                                      | 475 ms: 1.04x faster                                                       |
| meteor_contest            | 72.3 ms                                                     | 70.1 ms: 1.03x faster                                                      |
| asyncio_tcp               | 654 ms                                                      | 638 ms: 1.02x faster                                                       |
| xml_etree_generate        | 53.3 ms                                                     | 52.6 ms: 1.01x faster                                                      |
| pickle_pure_python        | 183 us                                                      | 181 us: 1.01x faster                                                       |
| xml_etree_iterparse       | 62.3 ms                                                     | 61.5 ms: 1.01x faster                                                      |
| pprint_pformat            | 991 ms                                                      | 983 ms: 1.01x faster                                                       |
| python_startup            | 22.2 ms                                                     | 22.0 ms: 1.01x faster                                                      |
| coverage                  | 46.7 ms                                                     | 47.1 ms: 1.01x slower                                                      |
| pidigits                  | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| gc_traversal              | 1.55 ms                                                     | 1.57 ms: 1.01x slower                                                      |
| pathlib                   | 81.2 ms                                                     | 82.1 ms: 1.01x slower                                                      |
| mdp                       | 1.38 sec                                                    | 1.41 sec: 1.02x slower                                                     |
| python_startup_no_site    | 17.8 ms                                                     | 18.2 ms: 1.02x slower                                                      |
| xml_etree_process         | 36.5 ms                                                     | 37.5 ms: 1.03x slower                                                      |
| scimark_lu                | 54.0 ms                                                     | 55.6 ms: 1.03x slower                                                      |
| chaos                     | 37.9 ms                                                     | 39.0 ms: 1.03x slower                                                      |
| logging_format            | 6.15 us                                                     | 6.36 us: 1.03x slower                                                      |
| tornado_http              | 92.8 ms                                                     | 96.1 ms: 1.03x slower                                                      |
| logging_simple            | 5.72 us                                                     | 5.95 us: 1.04x slower                                                      |
| json_dumps                | 5.76 ms                                                     | 5.99 ms: 1.04x slower                                                      |
| async_tree_io_tg          | 512 ms                                                      | 537 ms: 1.05x slower                                                       |
| regex_v8                  | 14.7 ms                                                     | 15.4 ms: 1.05x slower                                                      |
| bench_mp_pool             | 69.6 ms                                                     | 73.7 ms: 1.06x slower                                                      |
| async_tree_io             | 521 ms                                                      | 551 ms: 1.06x slower                                                       |
| regex_dna                 | 114 ms                                                      | 122 ms: 1.06x slower                                                       |
| html5lib                  | 38.6 ms                                                     | 41.0 ms: 1.06x slower                                                      |
| dulwich_log               | 40.4 ms                                                     | 43.1 ms: 1.07x slower                                                      |
| generators                | 19.5 ms                                                     | 20.8 ms: 1.07x slower                                                      |
| unpickle_pure_python      | 127 us                                                      | 136 us: 1.07x slower                                                       |
| sqlglot_parse             | 761 us                                                      | 834 us: 1.10x slower                                                       |
| 2to3                      | 217 ms                                                      | 240 ms: 1.11x slower                                                       |
| logging_silent            | 51.0 ns                                                     | 56.5 ns: 1.11x slower                                                      |
| create_gc_cycles          | 829 us                                                      | 919 us: 1.11x slower                                                       |
| nqueens                   | 55.5 ms                                                     | 61.9 ms: 1.11x slower                                                      |
| sqlglot_optimize          | 33.1 ms                                                     | 36.9 ms: 1.11x slower                                                      |
| regex_compile             | 80.1 ms                                                     | 89.4 ms: 1.12x slower                                                      |
| coroutines                | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| sympy_sum                 | 86.4 ms                                                     | 97.3 ms: 1.13x slower                                                      |
| sympy_str                 | 166 ms                                                      | 188 ms: 1.13x slower                                                       |
| sqlglot_transpile         | 952 us                                                      | 1.08 ms: 1.13x slower                                                      |
| django_template           | 21.8 ms                                                     | 24.7 ms: 1.14x slower                                                      |
| sqlglot_normalize         | 171 ms                                                      | 195 ms: 1.14x slower                                                       |
| async_generators          | 223 ms                                                      | 256 ms: 1.15x slower                                                       |
| sympy_expand              | 285 ms                                                      | 332 ms: 1.16x slower                                                       |
| docutils                  | 1.57 sec                                                    | 1.84 sec: 1.17x slower                                                     |
| richards_super            | 29.3 ms                                                     | 34.5 ms: 1.18x slower                                                      |
| richards                  | 26.0 ms                                                     | 30.6 ms: 1.18x slower                                                      |
| go                        | 84.6 ms                                                     | 101 ms: 1.19x slower                                                       |
| genshi_xml                | 32.8 ms                                                     | 39.0 ms: 1.19x slower                                                      |
| pylint                    | 211 ms                                                      | 252 ms: 1.20x slower                                                       |
| sympy_integrate           | 12.3 ms                                                     | 14.7 ms: 1.20x slower                                                      |
| typing_runtime_protocols  | 100 us                                                      | 121 us: 1.20x slower                                                       |
| genshi_text               | 14.9 ms                                                     | 17.9 ms: 1.20x slower                                                      |
| raytrace                  | 156 ms                                                      | 188 ms: 1.20x slower                                                       |
| deltablue                 | 1.86 ms                                                     | 2.36 ms: 1.26x slower                                                      |
| hexiom                    | 3.69 ms                                                     | 4.69 ms: 1.27x slower                                                      |
| Geometric mean            | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (9): pycparser, xml_etree_parse, json_loads, bench_thread_pool, comprehensions, regex_effbot, async_tree_cpu_io_mixed_tg, json, async_tree_cpu_io_mixed
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 97.87% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown