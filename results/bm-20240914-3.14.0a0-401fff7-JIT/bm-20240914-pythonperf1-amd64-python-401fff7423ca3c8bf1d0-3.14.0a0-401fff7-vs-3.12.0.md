# Results vs. 3.12.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-amd64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.05x faster
- HPT reliability: 97.21%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 239 ms: 1.10x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.91 sec: 1.15x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 87.4 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 197 ms: 1.45x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 257 ms: 1.43x faster                                                       |
| async_tree_none            | 291 ms                                                      | 206 ms: 1.41x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 555 ms: 1.39x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 258 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 397 ms: 1.26x faster                                                       |
| async_tree_io              | 731 ms                                                      | 583 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 394 ms: 1.24x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.34x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 49.4 ms: 1.45x faster                                                      |
| float          | 56.8 ms                                                     | 44.5 ms: 1.28x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 121 ms: 1.05x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.9 ms: 1.05x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 94.2 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 49.0 ms: 1.14x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.26 sec: 1.09x faster                                                     |
| xml_etree_process    | 37.7 ms                                                     | 34.8 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.7 ms: 1.07x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 17.9 us: 1.03x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 92.4 ms: 1.01x faster                                                      |
| pickle               | 7.43 us                                                     | 7.38 us: 1.01x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.73 ms: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.87 us: 1.04x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 145 us: 1.09x slower                                                       |
| unpickle             | 8.18 us                                                     | 9.27 us: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (2): pickle_list, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.0 ms: 1.10x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.6 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.26 ms: 1.35x faster                                                      |
| django_template | 22.9 ms                                                     | 26.2 ms: 1.14x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 14.8 us: 1.60x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 43.3 ms: 1.54x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.39 sec: 1.51x faster                                                     |
| nbody                      | 71.9 ms                                                     | 49.4 ms: 1.45x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 197 ms: 1.45x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 257 ms: 1.43x faster                                                       |
| async_tree_none            | 291 ms                                                      | 206 ms: 1.41x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 555 ms: 1.39x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.26 ms: 1.35x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.32x faster                                                      |
| deepcopy                   | 238 us                                                      | 181 us: 1.32x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 258 ms: 1.32x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 60.7 ms: 1.30x faster                                                      |
| float                      | 56.8 ms                                                     | 44.5 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 397 ms: 1.26x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 38.6 ms: 1.26x faster                                                      |
| async_tree_io              | 731 ms                                                      | 583 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 394 ms: 1.24x faster                                                       |
| scimark_fft                | 184 ms                                                      | 149 ms: 1.24x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.13 ms: 1.20x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 1.82 ms: 1.19x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.79 us: 1.17x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 49.0 ms: 1.14x faster                                                      |
| pyflate                    | 295 ms                                                      | 265 ms: 1.11x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.26 sec: 1.09x faster                                                     |
| xml_etree_process          | 37.7 ms                                                     | 34.8 ms: 1.08x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.0 ms: 1.08x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 54.4 ms: 1.08x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 74.8 ms: 1.08x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.7 ms: 1.07x faster                                                      |
| generators                 | 22.5 ms                                                     | 21.1 ms: 1.07x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 809 us: 1.06x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 57.2 ns: 1.06x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 59.6 ms: 1.05x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 463 ms: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.3 ms: 1.05x faster                                                      |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.05x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.45 us: 1.04x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.06 us: 1.04x faster                                                      |
| json                       | 3.05 ms                                                     | 2.95 ms: 1.03x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.03x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 17.9 us: 1.03x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 42.7 ms: 1.02x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 87.4 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 503 ms: 1.02x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.03 sec: 1.01x faster                                                     |
| xml_etree_parse            | 93.0 ms                                                     | 92.4 ms: 1.01x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.38 us: 1.01x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 74.9 ms: 1.00x slower                                                      |
| fannkuch                   | 247 ms                                                      | 248 ms: 1.00x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.73 ms: 1.01x slower                                                      |
| go                         | 91.6 ms                                                     | 92.2 ms: 1.01x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                      |
| pycparser                  | 699 ms                                                      | 715 ms: 1.02x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 71.7 ms: 1.04x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.87 us: 1.04x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                     |
| regex_v8                   | 14.2 ms                                                     | 14.9 ms: 1.05x slower                                                      |
| raytrace                   | 192 ms                                                      | 202 ms: 1.05x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 199 ms: 1.06x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 97.9 ms: 1.07x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 94.2 ms: 1.08x slower                                                      |
| sympy_str                  | 175 ms                                                      | 189 ms: 1.08x slower                                                       |
| async_generators           | 239 ms                                                      | 260 ms: 1.08x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 145 us: 1.09x slower                                                       |
| 2to3                       | 218 ms                                                      | 239 ms: 1.10x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 886 us: 1.10x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.0 ms: 1.10x slower                                                      |
| python_startup             | 19.5 ms                                                     | 21.6 ms: 1.11x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.60 ms: 1.11x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.14 ms: 1.12x slower                                                      |
| unpickle                   | 8.18 us                                                     | 9.27 us: 1.13x slower                                                      |
| django_template            | 22.9 ms                                                     | 26.2 ms: 1.14x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.8 ms: 1.15x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 39.7 ms: 1.15x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.91 sec: 1.15x slower                                                     |
| sympy_expand               | 284 ms                                                      | 330 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.16x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.1 ms: 1.18x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.89 ms: 1.19x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 901 us: 1.20x slower                                                       |
| richards_super             | 32.1 ms                                                     | 39.1 ms: 1.22x slower                                                      |
| richards                   | 28.4 ms                                                     | 36.5 ms: 1.29x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 56.9 ns: 1.52x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (2): pickle_list, pickle_pure_python
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 97.21% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown