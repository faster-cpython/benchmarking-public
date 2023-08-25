
# Results vs. 3.11.0

- fork: python
- ref: 7b14c2ef194b6eed7967
- machine: darwin-arm64
- commit hash: 7b14c2e
- commit date: 2023-01-16
- overall geometric mean: 1.00x faster \*
- HPT reliability: 73.92%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-darwin-arm64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 163 ms: 1.01x slower                                                   |
| chameleon      | 4.60 ms                                                | 4.57 ms: 1.01x faster                                                  |
| docutils       | 1.47 sec                                               | 1.46 sec: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-darwin-arm64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 53.0 ms                                                | 51.7 ms: 1.02x faster                                                  |
| nbody          | 65.6 ms                                                | 64.1 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-darwin-arm64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 74.6 ms: 1.03x faster                                                  |
| regex_v8       | 16.1 ms                                                | 15.7 ms: 1.03x faster                                                  |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                                   |
| regex_effbot   | 2.63 ms                                                | 2.62 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-darwin-arm64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.15 ms: 1.24x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 96.9 ms: 1.11x faster                                                  |
| unpickle_pure_python | 159 us                                                 | 144 us: 1.11x faster                                                   |
| pickle_pure_python   | 201 us                                                 | 193 us: 1.04x faster                                                   |
| xml_etree_process    | 35.1 ms                                                | 35.0 ms: 1.00x faster                                                  |
| json_loads           | 16.1 us                                                | 16.2 us: 1.00x slower                                                  |
| pickle_list          | 2.81 us                                                | 2.85 us: 1.01x slower                                                  |
| unpickle_list        | 2.65 us                                                | 2.73 us: 1.03x slower                                                  |
| pickle               | 7.15 us                                                | 7.50 us: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (4): xml_etree_iterparse, xml_etree_generate, pickle_dict, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-darwin-arm64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 12.4 ms: 1.00x faster                                                  |
| python_startup_no_site | 10.2 ms                                                | 10.4 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-darwin-arm64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 29.8 ms                                                | 28.2 ms: 1.06x faster                                                  |
| mako            | 8.53 ms                                                | 8.14 ms: 1.05x faster                                                  |
| django_template | 21.0 ms                                                | 21.7 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-darwin-arm64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 464 ms: 1.40x faster                                                   |
| json_dumps              | 7.63 ms                                                | 6.15 ms: 1.24x faster                                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.80 ms: 1.14x faster                                                  |
| xml_etree_parse         | 108 ms                                                 | 96.9 ms: 1.11x faster                                                  |
| unpickle_pure_python    | 159 us                                                 | 144 us: 1.11x faster                                                   |
| deltablue               | 2.81 ms                                                | 2.63 ms: 1.07x faster                                                  |
| genshi_xml              | 29.8 ms                                                | 28.2 ms: 1.06x faster                                                  |
| coverage                | 58.4 ms                                                | 55.4 ms: 1.05x faster                                                  |
| scimark_sor             | 82.6 ms                                                | 78.5 ms: 1.05x faster                                                  |
| mako                    | 8.53 ms                                                | 8.14 ms: 1.05x faster                                                  |
| richards                | 32.2 ms                                                | 30.8 ms: 1.05x faster                                                  |
| unpack_sequence         | 34.1 ns                                                | 32.7 ns: 1.04x faster                                                  |
| pickle_pure_python      | 201 us                                                 | 193 us: 1.04x faster                                                   |
| pycparser               | 698 ms                                                 | 673 ms: 1.04x faster                                                   |
| logging_silent          | 68.1 ns                                                | 66.1 ns: 1.03x faster                                                  |
| fannkuch                | 261 ms                                                 | 254 ms: 1.03x faster                                                   |
| regex_compile           | 76.7 ms                                                | 74.6 ms: 1.03x faster                                                  |
| regex_v8                | 16.1 ms                                                | 15.7 ms: 1.03x faster                                                  |
| float                   | 53.0 ms                                                | 51.7 ms: 1.02x faster                                                  |
| bench_thread_pool       | 474 us                                                 | 464 us: 1.02x faster                                                   |
| create_gc_cycles        | 716 us                                                 | 700 us: 1.02x faster                                                   |
| nbody                   | 65.6 ms                                                | 64.1 ms: 1.02x faster                                                  |
| scimark_fft             | 200 ms                                                 | 195 ms: 1.02x faster                                                   |
| dulwich_log             | 30.3 ms                                                | 29.7 ms: 1.02x faster                                                  |
| mdp                     | 1.55 sec                                               | 1.51 sec: 1.02x faster                                                 |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                                   |
| logging_simple          | 3.55 us                                                | 3.49 us: 1.02x faster                                                  |
| deepcopy_memo           | 26.3 us                                                | 26.0 us: 1.01x faster                                                  |
| scimark_lu              | 73.3 ms                                                | 72.6 ms: 1.01x faster                                                  |
| docutils                | 1.47 sec                                               | 1.46 sec: 1.01x faster                                                 |
| pprint_pformat          | 954 ms                                                 | 945 ms: 1.01x faster                                                   |
| chameleon               | 4.60 ms                                                | 4.57 ms: 1.01x faster                                                  |
| regex_effbot            | 2.63 ms                                                | 2.62 ms: 1.01x faster                                                  |
| sympy_integrate         | 11.5 ms                                                | 11.5 ms: 1.00x faster                                                  |
| sympy_expand            | 242 ms                                                 | 241 ms: 1.00x faster                                                   |
| thrift                  | 442 us                                                 | 440 us: 1.00x faster                                                   |
| pprint_safe_repr        | 466 ms                                                 | 465 ms: 1.00x faster                                                   |
| xml_etree_process       | 35.1 ms                                                | 35.0 ms: 1.00x faster                                                  |
| go                      | 109 ms                                                 | 108 ms: 1.00x faster                                                   |
| python_startup          | 12.4 ms                                                | 12.4 ms: 1.00x faster                                                  |
| gc_traversal            | 2.42 ms                                                | 2.42 ms: 1.00x slower                                                  |
| json_loads              | 16.1 us                                                | 16.2 us: 1.00x slower                                                  |
| logging_format          | 3.78 us                                                | 3.80 us: 1.01x slower                                                  |
| 2to3                    | 161 ms                                                 | 163 ms: 1.01x slower                                                   |
| sqlglot_optimize        | 31.1 ms                                                | 31.4 ms: 1.01x slower                                                  |
| sqlglot_normalize       | 171 ms                                                 | 172 ms: 1.01x slower                                                   |
| async_tree_none         | 286 ms                                                 | 289 ms: 1.01x slower                                                   |
| sympy_sum               | 85.5 ms                                                | 86.6 ms: 1.01x slower                                                  |
| pickle_list             | 2.81 us                                                | 2.85 us: 1.01x slower                                                  |
| hexiom                  | 4.72 ms                                                | 4.79 ms: 1.01x slower                                                  |
| spectral_norm           | 72.6 ms                                                | 73.7 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed | 533 ms                                                 | 543 ms: 1.02x slower                                                   |
| pyflate                 | 310 ms                                                 | 316 ms: 1.02x slower                                                   |
| python_startup_no_site  | 10.2 ms                                                | 10.4 ms: 1.02x slower                                                  |
| crypto_pyaes            | 51.7 ms                                                | 52.9 ms: 1.02x slower                                                  |
| chaos                   | 49.4 ms                                                | 50.7 ms: 1.03x slower                                                  |
| unpickle_list           | 2.65 us                                                | 2.73 us: 1.03x slower                                                  |
| async_generators        | 196 ms                                                 | 202 ms: 1.03x slower                                                   |
| meteor_contest          | 73.5 ms                                                | 75.6 ms: 1.03x slower                                                  |
| telco                   | 3.41 ms                                                | 3.51 ms: 1.03x slower                                                  |
| nqueens                 | 59.8 ms                                                | 61.7 ms: 1.03x slower                                                  |
| django_template         | 21.0 ms                                                | 21.7 ms: 1.03x slower                                                  |
| pickle                  | 7.15 us                                                | 7.50 us: 1.05x slower                                                  |
| coroutines              | 17.8 ms                                                | 18.7 ms: 1.05x slower                                                  |
| raytrace                | 207 ms                                                 | 219 ms: 1.06x slower                                                   |
| sqlite_synth            | 1.27 us                                                | 1.34 us: 1.06x slower                                                  |
| async_tree_io           | 704 ms                                                 | 750 ms: 1.06x slower                                                   |
| sqlglot_transpile       | 1.12 ms                                                | 1.20 ms: 1.07x slower                                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 49.8 ms: 1.07x slower                                                  |
| sqlglot_parse           | 959 us                                                 | 1.04 ms: 1.08x slower                                                  |
| comprehensions          | 16.1 us                                                | 17.8 us: 1.10x slower                                                  |
| generators              | 28.8 ms                                                | 33.9 ms: 1.18x slower                                                  |
| mypy2                   | 195 ms                                                 | 263 ms: 1.35x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (15): tornado_http, async_tree_memoization, genshi_text, xml_etree_iterparse, xml_etree_generate, pidigits, deepcopy, deepcopy_reduce, json, sympy_str, pickle_dict, html5lib, unpickle, bench_mp_pool, pathlib
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230116-3.12.0a4+-7b14c2e/bm-20230116-darwin-arm64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e.json: dask


# HPT report

- Reliability score: 73.92% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
