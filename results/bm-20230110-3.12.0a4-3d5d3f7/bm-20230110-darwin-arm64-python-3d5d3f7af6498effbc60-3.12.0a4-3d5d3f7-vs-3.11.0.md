
# Results vs. 3.11.0

- fork: python
- ref: 3d5d3f7af6498effbc60
- machine: darwin-arm64
- commit hash: 3d5d3f7
- commit date: 2023-01-10
- overall geometric mean: 1.00x faster \*
- HPT reliability: 69.13%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 163 ms: 1.01x slower                                                  |
| chameleon      | 4.60 ms                                                | 4.53 ms: 1.01x faster                                                 |
| docutils       | 1.47 sec                                               | 1.45 sec: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 63.9 ms: 1.03x faster                                                 |
| float          | 53.0 ms                                                | 52.0 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 74.5 ms: 1.03x faster                                                 |
| regex_v8       | 16.1 ms                                                | 15.7 ms: 1.03x faster                                                 |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.61 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.05 ms: 1.26x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 96.5 ms: 1.12x faster                                                 |
| unpickle_pure_python | 159 us                                                 | 143 us: 1.12x faster                                                  |
| pickle_pure_python   | 201 us                                                 | 192 us: 1.04x faster                                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 69.4 ms: 1.01x faster                                                 |
| xml_etree_process    | 35.1 ms                                                | 34.9 ms: 1.00x faster                                                 |
| json_loads           | 16.1 us                                                | 16.2 us: 1.01x slower                                                 |
| xml_etree_generate   | 48.3 ms                                                | 48.6 ms: 1.01x slower                                                 |
| pickle_list          | 2.81 us                                                | 2.83 us: 1.01x slower                                                 |
| unpickle             | 9.67 us                                                | 9.76 us: 1.01x slower                                                 |
| unpickle_list        | 2.65 us                                                | 2.70 us: 1.02x slower                                                 |
| pickle               | 7.15 us                                                | 7.44 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 12.3 ms: 1.01x faster                                                 |
| python_startup_no_site | 10.2 ms                                                | 10.2 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 8.12 ms: 1.05x faster                                                 |
| genshi_xml      | 29.8 ms                                                | 28.4 ms: 1.05x faster                                                 |
| django_template | 21.0 ms                                                | 21.6 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 449 ms: 1.45x faster                                                  |
| json_dumps              | 7.63 ms                                                | 6.05 ms: 1.26x faster                                                 |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.81 ms: 1.14x faster                                                 |
| xml_etree_parse         | 108 ms                                                 | 96.5 ms: 1.12x faster                                                 |
| unpickle_pure_python    | 159 us                                                 | 143 us: 1.12x faster                                                  |
| deltablue               | 2.81 ms                                                | 2.64 ms: 1.07x faster                                                 |
| richards                | 32.2 ms                                                | 30.6 ms: 1.05x faster                                                 |
| mako                    | 8.53 ms                                                | 8.12 ms: 1.05x faster                                                 |
| genshi_xml              | 29.8 ms                                                | 28.4 ms: 1.05x faster                                                 |
| unpack_sequence         | 34.1 ns                                                | 32.7 ns: 1.04x faster                                                 |
| pickle_pure_python      | 201 us                                                 | 192 us: 1.04x faster                                                  |
| create_gc_cycles        | 716 us                                                 | 692 us: 1.03x faster                                                  |
| logging_simple          | 3.55 us                                                | 3.44 us: 1.03x faster                                                 |
| pycparser               | 698 ms                                                 | 676 ms: 1.03x faster                                                  |
| regex_compile           | 76.7 ms                                                | 74.5 ms: 1.03x faster                                                 |
| fannkuch                | 261 ms                                                 | 254 ms: 1.03x faster                                                  |
| nbody                   | 65.6 ms                                                | 63.9 ms: 1.03x faster                                                 |
| regex_v8                | 16.1 ms                                                | 15.7 ms: 1.03x faster                                                 |
| bench_thread_pool       | 474 us                                                 | 462 us: 1.03x faster                                                  |
| logging_silent          | 68.1 ns                                                | 66.4 ns: 1.03x faster                                                 |
| scimark_fft             | 200 ms                                                 | 195 ms: 1.02x faster                                                  |
| dulwich_log             | 30.3 ms                                                | 29.6 ms: 1.02x faster                                                 |
| coverage                | 58.4 ms                                                | 57.2 ms: 1.02x faster                                                 |
| float                   | 53.0 ms                                                | 52.0 ms: 1.02x faster                                                 |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                                  |
| pprint_pformat          | 954 ms                                                 | 939 ms: 1.02x faster                                                  |
| chameleon               | 4.60 ms                                                | 4.53 ms: 1.01x faster                                                 |
| python_startup          | 12.4 ms                                                | 12.3 ms: 1.01x faster                                                 |
| docutils                | 1.47 sec                                               | 1.45 sec: 1.01x faster                                                |
| logging_format          | 3.78 us                                                | 3.74 us: 1.01x faster                                                 |
| pprint_safe_repr        | 466 ms                                                 | 462 ms: 1.01x faster                                                  |
| sympy_integrate         | 11.5 ms                                                | 11.4 ms: 1.01x faster                                                 |
| xml_etree_iterparse     | 70.1 ms                                                | 69.4 ms: 1.01x faster                                                 |
| deepcopy                | 223 us                                                 | 221 us: 1.01x faster                                                  |
| scimark_lu              | 73.3 ms                                                | 72.7 ms: 1.01x faster                                                 |
| regex_effbot            | 2.63 ms                                                | 2.61 ms: 1.01x faster                                                 |
| thrift                  | 442 us                                                 | 438 us: 1.01x faster                                                  |
| xml_etree_process       | 35.1 ms                                                | 34.9 ms: 1.00x faster                                                 |
| deepcopy_memo           | 26.3 us                                                | 26.2 us: 1.00x faster                                                 |
| telco                   | 3.41 ms                                                | 3.39 ms: 1.00x faster                                                 |
| mdp                     | 1.55 sec                                               | 1.54 sec: 1.00x faster                                                |
| go                      | 109 ms                                                 | 109 ms: 1.00x slower                                                  |
| scimark_sor             | 82.6 ms                                                | 82.8 ms: 1.00x slower                                                 |
| python_startup_no_site  | 10.2 ms                                                | 10.2 ms: 1.00x slower                                                 |
| sympy_sum               | 85.5 ms                                                | 85.9 ms: 1.00x slower                                                 |
| json_loads              | 16.1 us                                                | 16.2 us: 1.01x slower                                                 |
| sqlglot_optimize        | 31.1 ms                                                | 31.3 ms: 1.01x slower                                                 |
| xml_etree_generate      | 48.3 ms                                                | 48.6 ms: 1.01x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 172 ms: 1.01x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 1.92 us: 1.01x slower                                                 |
| 2to3                    | 161 ms                                                 | 163 ms: 1.01x slower                                                  |
| pickle_list             | 2.81 us                                                | 2.83 us: 1.01x slower                                                 |
| async_tree_none         | 286 ms                                                 | 288 ms: 1.01x slower                                                  |
| unpickle                | 9.67 us                                                | 9.76 us: 1.01x slower                                                 |
| spectral_norm           | 72.6 ms                                                | 73.4 ms: 1.01x slower                                                 |
| nqueens                 | 59.8 ms                                                | 60.5 ms: 1.01x slower                                                 |
| crypto_pyaes            | 51.7 ms                                                | 52.6 ms: 1.02x slower                                                 |
| pathlib                 | 27.2 ms                                                | 27.8 ms: 1.02x slower                                                 |
| unpickle_list           | 2.65 us                                                | 2.70 us: 1.02x slower                                                 |
| async_generators        | 196 ms                                                 | 200 ms: 1.02x slower                                                  |
| meteor_contest          | 73.5 ms                                                | 75.1 ms: 1.02x slower                                                 |
| chaos                   | 49.4 ms                                                | 50.5 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed | 533 ms                                                 | 546 ms: 1.02x slower                                                  |
| pyflate                 | 310 ms                                                 | 318 ms: 1.03x slower                                                  |
| django_template         | 21.0 ms                                                | 21.6 ms: 1.03x slower                                                 |
| pickle                  | 7.15 us                                                | 7.44 us: 1.04x slower                                                 |
| hexiom                  | 4.72 ms                                                | 4.94 ms: 1.05x slower                                                 |
| raytrace                | 207 ms                                                 | 217 ms: 1.05x slower                                                  |
| coroutines              | 17.8 ms                                                | 18.7 ms: 1.05x slower                                                 |
| gc_traversal            | 2.42 ms                                                | 2.56 ms: 1.06x slower                                                 |
| async_tree_io           | 704 ms                                                 | 748 ms: 1.06x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.35 us: 1.06x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                | 1.20 ms: 1.07x slower                                                 |
| scimark_monte_carlo     | 46.5 ms                                                | 49.6 ms: 1.07x slower                                                 |
| sqlglot_parse           | 959 us                                                 | 1.04 ms: 1.08x slower                                                 |
| comprehensions          | 16.1 us                                                | 17.7 us: 1.10x slower                                                 |
| generators              | 28.8 ms                                                | 33.7 ms: 1.17x slower                                                 |
| mypy2                   | 195 ms                                                 | 263 ms: 1.35x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (9): async_tree_memoization, genshi_text, sympy_expand, sympy_str, pickle_dict, pidigits, bench_mp_pool, json, html5lib
Ignored benchmarks (11) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230110-3.12.0a4-3d5d3f7/bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7.json: dask


# HPT report

- Reliability score: 69.13% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
