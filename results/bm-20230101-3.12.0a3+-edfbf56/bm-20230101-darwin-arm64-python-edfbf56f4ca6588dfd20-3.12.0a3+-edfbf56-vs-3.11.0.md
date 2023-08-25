
# Results vs. 3.11.0

- fork: python
- ref: edfbf56f4ca6588dfd20
- machine: darwin-arm64
- commit hash: edfbf56
- commit date: 2023-01-01
- overall geometric mean: 1.00x faster \*
- HPT reliability: 60.84%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 163 ms: 1.01x slower                                                   |
| chameleon      | 4.60 ms                                                | 4.56 ms: 1.01x faster                                                  |
| docutils       | 1.47 sec                                               | 1.46 sec: 1.00x faster                                                 |
| html5lib       | 34.7 ms                                                | 34.1 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 63.8 ms: 1.03x faster                                                  |
| float          | 53.0 ms                                                | 51.6 ms: 1.03x faster                                                  |
| pidigits       | 281 ms                                                 | 280 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 74.9 ms: 1.02x faster                                                  |
| regex_v8       | 16.1 ms                                                | 15.7 ms: 1.02x faster                                                  |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                                   |
| regex_effbot   | 2.63 ms                                                | 2.60 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.13 ms: 1.24x faster                                                  |
| unpickle_pure_python | 159 us                                                 | 142 us: 1.12x faster                                                   |
| xml_etree_parse      | 108 ms                                                 | 96.5 ms: 1.12x faster                                                  |
| pickle_pure_python   | 201 us                                                 | 193 us: 1.04x faster                                                   |
| unpickle             | 9.67 us                                                | 9.63 us: 1.00x faster                                                  |
| pickle_dict          | 18.0 us                                                | 18.0 us: 1.00x slower                                                  |
| xml_etree_process    | 35.1 ms                                                | 35.2 ms: 1.00x slower                                                  |
| xml_etree_generate   | 48.3 ms                                                | 48.5 ms: 1.00x slower                                                  |
| pickle_list          | 2.81 us                                                | 2.84 us: 1.01x slower                                                  |
| unpickle_list        | 2.65 us                                                | 2.70 us: 1.02x slower                                                  |
| pickle               | 7.15 us                                                | 7.46 us: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 12.3 ms: 1.01x faster                                                  |
| python_startup_no_site | 10.2 ms                                                | 10.3 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 29.8 ms                                                | 28.4 ms: 1.05x faster                                                  |
| mako            | 8.53 ms                                                | 8.15 ms: 1.05x faster                                                  |
| genshi_text     | 15.3 ms                                                | 15.0 ms: 1.02x faster                                                  |
| django_template | 21.0 ms                                                | 22.0 ms: 1.05x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 457 ms: 1.42x faster                                                   |
| json_dumps              | 7.63 ms                                                | 6.13 ms: 1.24x faster                                                  |
| unpickle_pure_python    | 159 us                                                 | 142 us: 1.12x faster                                                   |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.85 ms: 1.12x faster                                                  |
| xml_etree_parse         | 108 ms                                                 | 96.5 ms: 1.12x faster                                                  |
| deltablue               | 2.81 ms                                                | 2.62 ms: 1.08x faster                                                  |
| coverage                | 58.4 ms                                                | 54.6 ms: 1.07x faster                                                  |
| richards                | 32.2 ms                                                | 30.4 ms: 1.06x faster                                                  |
| logging_silent          | 68.1 ns                                                | 64.7 ns: 1.05x faster                                                  |
| genshi_xml              | 29.8 ms                                                | 28.4 ms: 1.05x faster                                                  |
| mako                    | 8.53 ms                                                | 8.15 ms: 1.05x faster                                                  |
| unpack_sequence         | 34.1 ns                                                | 32.7 ns: 1.04x faster                                                  |
| pickle_pure_python      | 201 us                                                 | 193 us: 1.04x faster                                                   |
| create_gc_cycles        | 716 us                                                 | 695 us: 1.03x faster                                                   |
| pycparser               | 698 ms                                                 | 678 ms: 1.03x faster                                                   |
| scimark_sor             | 82.6 ms                                                | 80.3 ms: 1.03x faster                                                  |
| nbody                   | 65.6 ms                                                | 63.8 ms: 1.03x faster                                                  |
| float                   | 53.0 ms                                                | 51.6 ms: 1.03x faster                                                  |
| dulwich_log             | 30.3 ms                                                | 29.6 ms: 1.03x faster                                                  |
| regex_compile           | 76.7 ms                                                | 74.9 ms: 1.02x faster                                                  |
| regex_v8                | 16.1 ms                                                | 15.7 ms: 1.02x faster                                                  |
| scimark_lu              | 73.3 ms                                                | 71.8 ms: 1.02x faster                                                  |
| logging_simple          | 3.55 us                                                | 3.47 us: 1.02x faster                                                  |
| deepcopy_memo           | 26.3 us                                                | 25.8 us: 1.02x faster                                                  |
| genshi_text             | 15.3 ms                                                | 15.0 ms: 1.02x faster                                                  |
| bench_thread_pool       | 474 us                                                 | 465 us: 1.02x faster                                                   |
| pprint_pformat          | 954 ms                                                 | 936 ms: 1.02x faster                                                   |
| fannkuch                | 261 ms                                                 | 257 ms: 1.02x faster                                                   |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                                   |
| html5lib                | 34.7 ms                                                | 34.1 ms: 1.02x faster                                                  |
| pprint_safe_repr        | 466 ms                                                 | 460 ms: 1.02x faster                                                   |
| scimark_fft             | 200 ms                                                 | 198 ms: 1.01x faster                                                   |
| regex_effbot            | 2.63 ms                                                | 2.60 ms: 1.01x faster                                                  |
| go                      | 109 ms                                                 | 108 ms: 1.01x faster                                                   |
| chameleon               | 4.60 ms                                                | 4.56 ms: 1.01x faster                                                  |
| deepcopy                | 223 us                                                 | 221 us: 1.01x faster                                                   |
| mdp                     | 1.55 sec                                               | 1.53 sec: 1.01x faster                                                 |
| python_startup          | 12.4 ms                                                | 12.3 ms: 1.01x faster                                                  |
| deepcopy_reduce         | 1.91 us                                                | 1.90 us: 1.01x faster                                                  |
| unpickle                | 9.67 us                                                | 9.63 us: 1.00x faster                                                  |
| docutils                | 1.47 sec                                               | 1.46 sec: 1.00x faster                                                 |
| logging_format          | 3.78 us                                                | 3.76 us: 1.00x faster                                                  |
| pidigits                | 281 ms                                                 | 280 ms: 1.00x faster                                                   |
| pickle_dict             | 18.0 us                                                | 18.0 us: 1.00x slower                                                  |
| xml_etree_process       | 35.1 ms                                                | 35.2 ms: 1.00x slower                                                  |
| xml_etree_generate      | 48.3 ms                                                | 48.5 ms: 1.00x slower                                                  |
| sympy_sum               | 85.5 ms                                                | 86.1 ms: 1.01x slower                                                  |
| 2to3                    | 161 ms                                                 | 163 ms: 1.01x slower                                                   |
| pickle_list             | 2.81 us                                                | 2.84 us: 1.01x slower                                                  |
| async_tree_none         | 286 ms                                                 | 289 ms: 1.01x slower                                                   |
| sympy_expand            | 242 ms                                                 | 245 ms: 1.01x slower                                                   |
| python_startup_no_site  | 10.2 ms                                                | 10.3 ms: 1.01x slower                                                  |
| sympy_str               | 151 ms                                                 | 153 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed | 533 ms                                                 | 543 ms: 1.02x slower                                                   |
| coroutines              | 17.8 ms                                                | 18.1 ms: 1.02x slower                                                  |
| unpickle_list           | 2.65 us                                                | 2.70 us: 1.02x slower                                                  |
| sqlglot_optimize        | 31.1 ms                                                | 31.8 ms: 1.02x slower                                                  |
| spectral_norm           | 72.6 ms                                                | 74.2 ms: 1.02x slower                                                  |
| async_generators        | 196 ms                                                 | 201 ms: 1.02x slower                                                   |
| sqlglot_normalize       | 171 ms                                                 | 175 ms: 1.02x slower                                                   |
| nqueens                 | 59.8 ms                                                | 61.6 ms: 1.03x slower                                                  |
| chaos                   | 49.4 ms                                                | 51.0 ms: 1.03x slower                                                  |
| telco                   | 3.41 ms                                                | 3.54 ms: 1.04x slower                                                  |
| meteor_contest          | 73.5 ms                                                | 76.4 ms: 1.04x slower                                                  |
| crypto_pyaes            | 51.7 ms                                                | 53.8 ms: 1.04x slower                                                  |
| pickle                  | 7.15 us                                                | 7.46 us: 1.04x slower                                                  |
| hexiom                  | 4.72 ms                                                | 4.93 ms: 1.05x slower                                                  |
| pyflate                 | 310 ms                                                 | 325 ms: 1.05x slower                                                   |
| raytrace                | 207 ms                                                 | 217 ms: 1.05x slower                                                   |
| django_template         | 21.0 ms                                                | 22.0 ms: 1.05x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.34 us: 1.06x slower                                                  |
| async_tree_io           | 704 ms                                                 | 750 ms: 1.07x slower                                                   |
| sqlglot_transpile       | 1.12 ms                                                | 1.20 ms: 1.07x slower                                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 49.8 ms: 1.07x slower                                                  |
| sqlglot_parse           | 959 us                                                 | 1.03 ms: 1.08x slower                                                  |
| comprehensions          | 16.1 us                                                | 17.9 us: 1.11x slower                                                  |
| generators              | 28.8 ms                                                | 33.2 ms: 1.16x slower                                                  |
| mypy2                   | 195 ms                                                 | 264 ms: 1.35x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (9): async_tree_memoization, xml_etree_iterparse, thrift, gc_traversal, json_loads, sympy_integrate, json, pathlib, bench_mp_pool
Ignored benchmarks (11) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230101-3.12.0a3+-edfbf56/bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56.json: dask


# HPT report

- Reliability score: 60.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
