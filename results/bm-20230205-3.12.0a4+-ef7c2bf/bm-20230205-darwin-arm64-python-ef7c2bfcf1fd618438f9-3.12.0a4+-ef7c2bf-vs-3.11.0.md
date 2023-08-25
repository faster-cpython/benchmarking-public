
# Results vs. 3.11.0

- fork: python
- ref: ef7c2bfcf1fd618438f9
- machine: darwin-arm64
- commit hash: ef7c2bf
- commit date: 2023-02-05
- overall geometric mean: 1.01x faster \*
- HPT reliability: 78.07%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-darwin-arm64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 163 ms: 1.01x slower                                                   |
| docutils       | 1.47 sec                                               | 1.46 sec: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (3): chameleon, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-darwin-arm64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 64.0 ms: 1.02x faster                                                  |
| float          | 53.0 ms                                                | 52.0 ms: 1.02x faster                                                  |
| pidigits       | 281 ms                                                 | 281 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-darwin-arm64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 72.4 ms: 1.06x faster                                                  |
| regex_v8       | 16.1 ms                                                | 15.7 ms: 1.03x faster                                                  |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                                   |
| regex_effbot   | 2.63 ms                                                | 2.63 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-darwin-arm64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.11 ms: 1.25x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 96.4 ms: 1.12x faster                                                  |
| pickle_pure_python   | 201 us                                                 | 191 us: 1.05x faster                                                   |
| pickle_list          | 2.81 us                                                | 2.74 us: 1.03x faster                                                  |
| unpickle_pure_python | 159 us                                                 | 156 us: 1.02x faster                                                   |
| xml_etree_process    | 35.1 ms                                                | 34.7 ms: 1.01x faster                                                  |
| xml_etree_generate   | 48.3 ms                                                | 48.0 ms: 1.01x faster                                                  |
| json_loads           | 16.1 us                                                | 16.1 us: 1.00x slower                                                  |
| unpickle_list        | 2.65 us                                                | 2.66 us: 1.00x slower                                                  |
| unpickle             | 9.67 us                                                | 9.87 us: 1.02x slower                                                  |
| pickle               | 7.15 us                                                | 7.46 us: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (2): pickle_dict, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-darwin-arm64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 12.5 ms: 1.01x slower                                                  |
| python_startup_no_site | 10.2 ms                                                | 10.4 ms: 1.03x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-darwin-arm64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.18 ms: 1.19x faster                                                  |
| genshi_text     | 15.3 ms                                                | 14.2 ms: 1.07x faster                                                  |
| genshi_xml      | 29.8 ms                                                | 28.3 ms: 1.05x faster                                                  |
| django_template | 21.0 ms                                                | 21.2 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-darwin-arm64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 459 ms: 1.42x faster                                                   |
| json_dumps              | 7.63 ms                                                | 6.11 ms: 1.25x faster                                                  |
| mako                    | 8.53 ms                                                | 7.18 ms: 1.19x faster                                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.80 ms: 1.14x faster                                                  |
| xml_etree_parse         | 108 ms                                                 | 96.4 ms: 1.12x faster                                                  |
| hexiom                  | 4.72 ms                                                | 4.32 ms: 1.09x faster                                                  |
| deltablue               | 2.81 ms                                                | 2.58 ms: 1.09x faster                                                  |
| richards                | 32.2 ms                                                | 29.8 ms: 1.08x faster                                                  |
| chaos                   | 49.4 ms                                                | 45.7 ms: 1.08x faster                                                  |
| comprehensions          | 16.1 us                                                | 15.0 us: 1.07x faster                                                  |
| genshi_text             | 15.3 ms                                                | 14.2 ms: 1.07x faster                                                  |
| regex_compile           | 76.7 ms                                                | 72.4 ms: 1.06x faster                                                  |
| genshi_xml              | 29.8 ms                                                | 28.3 ms: 1.05x faster                                                  |
| pickle_pure_python      | 201 us                                                 | 191 us: 1.05x faster                                                   |
| pycparser               | 698 ms                                                 | 666 ms: 1.05x faster                                                   |
| sympy_sum               | 85.5 ms                                                | 82.0 ms: 1.04x faster                                                  |
| unpack_sequence         | 34.1 ns                                                | 32.7 ns: 1.04x faster                                                  |
| scimark_fft             | 200 ms                                                 | 192 ms: 1.04x faster                                                   |
| sympy_str               | 151 ms                                                 | 146 ms: 1.04x faster                                                   |
| scimark_lu              | 73.3 ms                                                | 70.8 ms: 1.04x faster                                                  |
| logging_silent          | 68.1 ns                                                | 65.8 ns: 1.03x faster                                                  |
| sympy_integrate         | 11.5 ms                                                | 11.2 ms: 1.03x faster                                                  |
| create_gc_cycles        | 716 us                                                 | 693 us: 1.03x faster                                                   |
| dulwich_log             | 30.3 ms                                                | 29.5 ms: 1.03x faster                                                  |
| async_tree_memoization  | 336 ms                                                 | 327 ms: 1.03x faster                                                   |
| regex_v8                | 16.1 ms                                                | 15.7 ms: 1.03x faster                                                  |
| pickle_list             | 2.81 us                                                | 2.74 us: 1.03x faster                                                  |
| bench_thread_pool       | 474 us                                                 | 463 us: 1.02x faster                                                   |
| nbody                   | 65.6 ms                                                | 64.0 ms: 1.02x faster                                                  |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.03 ms: 1.02x faster                                                  |
| coverage                | 58.4 ms                                                | 57.3 ms: 1.02x faster                                                  |
| fannkuch                | 261 ms                                                 | 256 ms: 1.02x faster                                                   |
| unpickle_pure_python    | 159 us                                                 | 156 us: 1.02x faster                                                   |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                                   |
| deepcopy_memo           | 26.3 us                                                | 25.9 us: 1.02x faster                                                  |
| float                   | 53.0 ms                                                | 52.0 ms: 1.02x faster                                                  |
| deepcopy                | 223 us                                                 | 219 us: 1.01x faster                                                   |
| mdp                     | 1.55 sec                                               | 1.53 sec: 1.01x faster                                                 |
| xml_etree_process       | 35.1 ms                                                | 34.7 ms: 1.01x faster                                                  |
| docutils                | 1.47 sec                                               | 1.46 sec: 1.01x faster                                                 |
| xml_etree_generate      | 48.3 ms                                                | 48.0 ms: 1.01x faster                                                  |
| pidigits                | 281 ms                                                 | 281 ms: 1.00x slower                                                   |
| regex_effbot            | 2.63 ms                                                | 2.63 ms: 1.00x slower                                                  |
| gc_traversal            | 2.42 ms                                                | 2.42 ms: 1.00x slower                                                  |
| json_loads              | 16.1 us                                                | 16.1 us: 1.00x slower                                                  |
| sqlglot_normalize       | 171 ms                                                 | 171 ms: 1.00x slower                                                   |
| unpickle_list           | 2.65 us                                                | 2.66 us: 1.00x slower                                                  |
| thrift                  | 442 us                                                 | 443 us: 1.00x slower                                                   |
| sympy_expand            | 242 ms                                                 | 243 ms: 1.00x slower                                                   |
| sqlalchemy_declarative  | 62.6 ms                                                | 63.0 ms: 1.01x slower                                                  |
| python_startup          | 12.4 ms                                                | 12.5 ms: 1.01x slower                                                  |
| django_template         | 21.0 ms                                                | 21.2 ms: 1.01x slower                                                  |
| telco                   | 3.41 ms                                                | 3.43 ms: 1.01x slower                                                  |
| 2to3                    | 161 ms                                                 | 163 ms: 1.01x slower                                                   |
| pprint_pformat          | 954 ms                                                 | 961 ms: 1.01x slower                                                   |
| sqlglot_optimize        | 31.1 ms                                                | 31.4 ms: 1.01x slower                                                  |
| pprint_safe_repr        | 466 ms                                                 | 472 ms: 1.01x slower                                                   |
| go                      | 109 ms                                                 | 110 ms: 1.01x slower                                                   |
| nqueens                 | 59.8 ms                                                | 60.6 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed | 533 ms                                                 | 543 ms: 1.02x slower                                                   |
| logging_simple          | 3.55 us                                                | 3.62 us: 1.02x slower                                                  |
| async_generators        | 196 ms                                                 | 200 ms: 1.02x slower                                                   |
| unpickle                | 9.67 us                                                | 9.87 us: 1.02x slower                                                  |
| bench_mp_pool           | 43.9 ms                                                | 45.0 ms: 1.02x slower                                                  |
| pathlib                 | 27.2 ms                                                | 27.9 ms: 1.03x slower                                                  |
| python_startup_no_site  | 10.2 ms                                                | 10.4 ms: 1.03x slower                                                  |
| crypto_pyaes            | 51.7 ms                                                | 53.1 ms: 1.03x slower                                                  |
| logging_format          | 3.78 us                                                | 3.90 us: 1.03x slower                                                  |
| scimark_sor             | 82.6 ms                                                | 85.5 ms: 1.04x slower                                                  |
| meteor_contest          | 73.5 ms                                                | 76.2 ms: 1.04x slower                                                  |
| pickle                  | 7.15 us                                                | 7.46 us: 1.04x slower                                                  |
| async_tree_io           | 704 ms                                                 | 743 ms: 1.05x slower                                                   |
| coroutines              | 17.8 ms                                                | 18.8 ms: 1.06x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.19 ms: 1.06x slower                                                  |
| sqlglot_parse           | 959 us                                                 | 1.02 ms: 1.06x slower                                                  |
| pyflate                 | 310 ms                                                 | 331 ms: 1.07x slower                                                   |
| scimark_monte_carlo     | 46.5 ms                                                | 49.8 ms: 1.07x slower                                                  |
| raytrace                | 207 ms                                                 | 222 ms: 1.07x slower                                                   |
| sqlite_synth            | 1.27 us                                                | 1.36 us: 1.07x slower                                                  |
| generators              | 28.8 ms                                                | 34.4 ms: 1.19x slower                                                  |
| mypy2                   | 195 ms                                                 | 260 ms: 1.33x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (9): tornado_http, chameleon, async_tree_none, pickle_dict, html5lib, xml_etree_iterparse, deepcopy_reduce, spectral_norm, json
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230205-3.12.0a4+-ef7c2bf/bm-20230205-darwin-arm64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf.json: dask


# HPT report

- Reliability score: 78.07% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
