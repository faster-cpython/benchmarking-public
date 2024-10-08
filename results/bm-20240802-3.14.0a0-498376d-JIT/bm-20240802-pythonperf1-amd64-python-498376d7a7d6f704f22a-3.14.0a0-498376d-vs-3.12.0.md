# Results vs. 3.12.0

- fork: python
- ref: 498376d7a7d6f704f22a
- machine: windows-amd64
- commit hash: 498376d
- commit date: 2024-08-02
- overall geometric mean: 1.06x faster
- HPT reliability: 94.91%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 240 ms: 1.10x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.84 sec: 1.10x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 96.1 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 189 ms: 1.51x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 246 ms: 1.49x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 537 ms: 1.44x faster                                                       |
| async_tree_none            | 291 ms                                                      | 212 ms: 1.38x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 375 ms: 1.34x faster                                                       |
| async_tree_io              | 731 ms                                                      | 551 ms: 1.33x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 259 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 392 ms: 1.25x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.38x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 49.8 ms: 1.44x faster                                                      |
| float          | 56.8 ms                                                     | 44.9 ms: 1.26x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 122 ms: 1.04x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 89.4 ms: 1.02x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 15.4 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.25 sec: 1.10x faster                                                     |
| pickle_pure_python   | 195 us                                                      | 181 us: 1.08x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 52.6 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.5 ms: 1.06x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 37.5 ms: 1.01x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 136 us: 1.02x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 5.99 ms: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 4.96 ms: 1.43x faster                                                      |
| django_template | 22.9 ms                                                     | 24.7 ms: 1.08x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 189 ms: 1.51x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 246 ms: 1.49x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 16.2 us: 1.47x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 46.1 ms: 1.45x faster                                                      |
| nbody                      | 71.9 ms                                                     | 49.8 ms: 1.44x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 537 ms: 1.44x faster                                                       |
| mako                       | 7.09 ms                                                     | 4.96 ms: 1.43x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.2 us: 1.38x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.52 sec: 1.38x faster                                                     |
| async_tree_none            | 291 ms                                                      | 212 ms: 1.38x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 375 ms: 1.34x faster                                                       |
| async_tree_io              | 731 ms                                                      | 551 ms: 1.33x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 59.9 ms: 1.31x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 259 ms: 1.31x faster                                                       |
| deepcopy                   | 238 us                                                      | 183 us: 1.30x faster                                                       |
| float                      | 56.8 ms                                                     | 44.9 ms: 1.26x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 392 ms: 1.25x faster                                                       |
| scimark_fft                | 184 ms                                                      | 148 ms: 1.25x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.07 ms: 1.23x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 39.9 ms: 1.22x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.78 us: 1.18x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.5 ms: 1.16x faster                                                      |
| pyflate                    | 295 ms                                                      | 257 ms: 1.15x faster                                                       |
| fannkuch                   | 247 ms                                                      | 220 ms: 1.12x faster                                                       |
| chaos                      | 43.3 ms                                                     | 39.0 ms: 1.11x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.25 sec: 1.10x faster                                                     |
| generators                 | 22.5 ms                                                     | 20.8 ms: 1.08x faster                                                      |
| pickle_pure_python         | 195 us                                                      | 181 us: 1.08x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 475 ms: 1.08x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 56.5 ns: 1.07x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 70.1 ms: 1.06x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 983 ms: 1.06x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 52.6 ms: 1.06x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.5 ms: 1.06x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 55.6 ms: 1.06x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.36 us: 1.06x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.95 us: 1.06x faster                                                      |
| regex_dna                  | 126 ms                                                      | 122 ms: 1.04x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 825 us: 1.04x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 43.1 ms: 1.03x faster                                                      |
| raytrace                   | 192 ms                                                      | 188 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 61.9 ms: 1.01x faster                                                      |
| json                       | 3.05 ms                                                     | 3.00 ms: 1.01x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 37.5 ms: 1.01x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 82.1 ms: 1.02x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 89.4 ms: 1.02x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 136 us: 1.02x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                     |
| gc_traversal               | 1.52 ms                                                     | 1.57 ms: 1.03x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 834 us: 1.04x slower                                                       |
| pycparser                  | 699 ms                                                      | 726 ms: 1.04x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 195 ms: 1.04x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.99 ms: 1.05x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.08 ms: 1.06x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 97.3 ms: 1.06x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 73.7 ms: 1.07x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.9 ms: 1.07x slower                                                      |
| async_generators           | 239 ms                                                      | 256 ms: 1.07x slower                                                       |
| sympy_str                  | 175 ms                                                      | 188 ms: 1.07x slower                                                       |
| tornado_http               | 89.5 ms                                                     | 96.1 ms: 1.07x slower                                                      |
| richards_super             | 32.1 ms                                                     | 34.5 ms: 1.07x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.7 ms: 1.08x slower                                                      |
| richards                   | 28.4 ms                                                     | 30.6 ms: 1.08x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 15.4 ms: 1.08x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.36 ms: 1.09x slower                                                      |
| go                         | 91.6 ms                                                     | 101 ms: 1.10x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.54 ms: 1.10x slower                                                      |
| 2to3                       | 218 ms                                                      | 240 ms: 1.10x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.84 sec: 1.10x slower                                                     |
| python_startup_no_site     | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.7 ms: 1.13x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.69 ms: 1.14x slower                                                      |
| coverage                   | 40.8 ms                                                     | 47.1 ms: 1.15x slower                                                      |
| sympy_expand               | 284 ms                                                      | 332 ms: 1.17x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 919 us: 1.22x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 121 us: 1.27x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 638 ms: 1.31x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, regex_effbot
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240802-3.14.0a0-498376d-JIT/bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 94.91% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown