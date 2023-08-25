
# Results vs. 3.11.0

- fork: python
- ref: b6bd7ffcbc1ffaa68e34
- machine: darwin-arm64
- commit hash: b6bd7ff
- commit date: 2022-12-06
- overall geometric mean: 1.04x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 168 ms: 1.04x slower                                                  |
| chameleon      | 4.60 ms                                                | 4.53 ms: 1.02x faster                                                 |
| docutils       | 1.47 sec                                               | 1.48 sec: 1.01x slower                                                |
| html5lib       | 34.7 ms                                                | 36.4 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 65.3 ms: 1.00x faster                                                 |
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                                  |
| float          | 53.0 ms                                                | 57.9 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 16.1 ms                                                | 15.7 ms: 1.03x faster                                                 |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.61 ms: 1.01x faster                                                 |
| regex_compile  | 76.7 ms                                                | 77.2 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.12 ms: 1.25x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 96.7 ms: 1.12x faster                                                 |
| unpickle_list        | 2.65 us                                                | 2.57 us: 1.03x faster                                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 69.6 ms: 1.01x faster                                                 |
| unpickle             | 9.67 us                                                | 9.63 us: 1.00x faster                                                 |
| pickle_list          | 2.81 us                                                | 2.83 us: 1.01x slower                                                 |
| json_loads           | 16.1 us                                                | 16.3 us: 1.01x slower                                                 |
| unpickle_pure_python | 159 us                                                 | 161 us: 1.01x slower                                                  |
| xml_etree_process    | 35.1 ms                                                | 36.3 ms: 1.04x slower                                                 |
| xml_etree_generate   | 48.3 ms                                                | 50.4 ms: 1.04x slower                                                 |
| pickle               | 7.15 us                                                | 7.60 us: 1.06x slower                                                 |
| pickle_pure_python   | 201 us                                                 | 214 us: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 12.3 ms: 1.01x faster                                                 |
| python_startup_no_site | 10.2 ms                                                | 10.2 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.24 ms: 1.18x faster                                                 |
| genshi_text     | 15.3 ms                                                | 14.7 ms: 1.04x faster                                                 |
| genshi_xml      | 29.8 ms                                                | 30.4 ms: 1.02x slower                                                 |
| django_template | 21.0 ms                                                | 21.9 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps              | 7.63 ms                                                | 6.12 ms: 1.25x faster                                                 |
| mako                    | 8.53 ms                                                | 7.24 ms: 1.18x faster                                                 |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.78 ms: 1.15x faster                                                 |
| xml_etree_parse         | 108 ms                                                 | 96.7 ms: 1.12x faster                                                 |
| logging_silent          | 68.1 ns                                                | 64.2 ns: 1.06x faster                                                 |
| genshi_text             | 15.3 ms                                                | 14.7 ms: 1.04x faster                                                 |
| scimark_lu              | 73.3 ms                                                | 70.9 ms: 1.03x faster                                                 |
| create_gc_cycles        | 716 us                                                 | 694 us: 1.03x faster                                                  |
| unpickle_list           | 2.65 us                                                | 2.57 us: 1.03x faster                                                 |
| regex_v8                | 16.1 ms                                                | 15.7 ms: 1.03x faster                                                 |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                                  |
| chameleon               | 4.60 ms                                                | 4.53 ms: 1.02x faster                                                 |
| python_startup          | 12.4 ms                                                | 12.3 ms: 1.01x faster                                                 |
| regex_effbot            | 2.63 ms                                                | 2.61 ms: 1.01x faster                                                 |
| scimark_fft             | 200 ms                                                 | 198 ms: 1.01x faster                                                  |
| xml_etree_iterparse     | 70.1 ms                                                | 69.6 ms: 1.01x faster                                                 |
| nbody                   | 65.6 ms                                                | 65.3 ms: 1.00x faster                                                 |
| unpickle                | 9.67 us                                                | 9.63 us: 1.00x faster                                                 |
| bench_thread_pool       | 474 us                                                 | 473 us: 1.00x faster                                                  |
| pidigits                | 281 ms                                                 | 282 ms: 1.00x slower                                                  |
| python_startup_no_site  | 10.2 ms                                                | 10.2 ms: 1.00x slower                                                 |
| dulwich_log             | 30.3 ms                                                | 30.5 ms: 1.01x slower                                                 |
| regex_compile           | 76.7 ms                                                | 77.2 ms: 1.01x slower                                                 |
| pickle_list             | 2.81 us                                                | 2.83 us: 1.01x slower                                                 |
| docutils                | 1.47 sec                                               | 1.48 sec: 1.01x slower                                                |
| thrift                  | 442 us                                                 | 447 us: 1.01x slower                                                  |
| json_loads              | 16.1 us                                                | 16.3 us: 1.01x slower                                                 |
| unpickle_pure_python    | 159 us                                                 | 161 us: 1.01x slower                                                  |
| deltablue               | 2.81 ms                                                | 2.85 ms: 1.01x slower                                                 |
| json                    | 2.78 ms                                                | 2.82 ms: 1.01x slower                                                 |
| genshi_xml              | 29.8 ms                                                | 30.4 ms: 1.02x slower                                                 |
| pathlib                 | 27.2 ms                                                | 27.9 ms: 1.02x slower                                                 |
| spectral_norm           | 72.6 ms                                                | 74.4 ms: 1.03x slower                                                 |
| sympy_sum               | 85.5 ms                                                | 87.9 ms: 1.03x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 176 ms: 1.03x slower                                                  |
| sqlglot_optimize        | 31.1 ms                                                | 32.1 ms: 1.03x slower                                                 |
| sympy_str               | 151 ms                                                 | 157 ms: 1.04x slower                                                  |
| xml_etree_process       | 35.1 ms                                                | 36.3 ms: 1.04x slower                                                 |
| logging_simple          | 3.55 us                                                | 3.68 us: 1.04x slower                                                 |
| sympy_expand            | 242 ms                                                 | 251 ms: 1.04x slower                                                  |
| 2to3                    | 161 ms                                                 | 168 ms: 1.04x slower                                                  |
| async_tree_none         | 286 ms                                                 | 297 ms: 1.04x slower                                                  |
| coverage                | 58.4 ms                                                | 60.7 ms: 1.04x slower                                                 |
| nqueens                 | 59.8 ms                                                | 62.2 ms: 1.04x slower                                                 |
| django_template         | 21.0 ms                                                | 21.9 ms: 1.04x slower                                                 |
| chaos                   | 49.4 ms                                                | 51.5 ms: 1.04x slower                                                 |
| sympy_integrate         | 11.5 ms                                                | 12.0 ms: 1.04x slower                                                 |
| async_tree_cpu_io_mixed | 533 ms                                                 | 556 ms: 1.04x slower                                                  |
| xml_etree_generate      | 48.3 ms                                                | 50.4 ms: 1.04x slower                                                 |
| fannkuch                | 261 ms                                                 | 273 ms: 1.05x slower                                                  |
| sqlglot_parse           | 959 us                                                 | 1.00 ms: 1.05x slower                                                 |
| crypto_pyaes            | 51.7 ms                                                | 54.2 ms: 1.05x slower                                                 |
| logging_format          | 3.78 us                                                | 3.96 us: 1.05x slower                                                 |
| html5lib                | 34.7 ms                                                | 36.4 ms: 1.05x slower                                                 |
| async_generators        | 196 ms                                                 | 207 ms: 1.05x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.19 ms: 1.06x slower                                                 |
| hexiom                  | 4.72 ms                                                | 5.01 ms: 1.06x slower                                                 |
| pickle                  | 7.15 us                                                | 7.60 us: 1.06x slower                                                 |
| pickle_pure_python      | 201 us                                                 | 214 us: 1.07x slower                                                  |
| meteor_contest          | 73.5 ms                                                | 78.6 ms: 1.07x slower                                                 |
| raytrace                | 207 ms                                                 | 222 ms: 1.07x slower                                                  |
| async_tree_io           | 704 ms                                                 | 756 ms: 1.07x slower                                                  |
| mdp                     | 1.55 sec                                               | 1.66 sec: 1.07x slower                                                |
| pprint_safe_repr        | 466 ms                                                 | 502 ms: 1.08x slower                                                  |
| pprint_pformat          | 954 ms                                                 | 1.03 sec: 1.08x slower                                                |
| go                      | 109 ms                                                 | 118 ms: 1.09x slower                                                  |
| float                   | 53.0 ms                                                | 57.9 ms: 1.09x slower                                                 |
| sqlite_synth            | 1.27 us                                                | 1.40 us: 1.10x slower                                                 |
| comprehensions          | 16.1 us                                                | 17.8 us: 1.11x slower                                                 |
| coroutines              | 17.8 ms                                                | 19.9 ms: 1.12x slower                                                 |
| pyflate                 | 310 ms                                                 | 352 ms: 1.13x slower                                                  |
| deepcopy                | 223 us                                                 | 253 us: 1.14x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.17 us: 1.14x slower                                                 |
| generators              | 28.8 ms                                                | 33.6 ms: 1.17x slower                                                 |
| deepcopy_memo           | 26.3 us                                                | 31.0 us: 1.18x slower                                                 |
| scimark_monte_carlo     | 46.5 ms                                                | 56.2 ms: 1.21x slower                                                 |
| scimark_sor             | 82.6 ms                                                | 104 ms: 1.26x slower                                                  |
| mypy2                   | 195 ms                                                 | 264 ms: 1.36x slower                                                  |
| unpack_sequence         | 34.1 ns                                                | 52.7 ns: 1.54x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.04x slower                                                          |

Benchmark hidden because not significant (8): richards, async_tree_memoization, gc_traversal, telco, pickle_dict, asyncio_tcp, pycparser, bench_mp_pool
Ignored benchmarks (11) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221206-3.12.0a3-b6bd7ff/bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff.json: dask


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x
