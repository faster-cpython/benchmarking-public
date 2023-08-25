
# Results vs. 3.11.0

- fork: python
- ref: 14d4f68ebb495fe7ccba
- machine: darwin-arm64
- commit hash: 14d4f68
- commit date: 2022-10-02
- overall geometric mean: 1.00x slower \*
- HPT reliability: 97.27%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 185 ms: 1.15x slower                                                  |
| chameleon      | 4.60 ms                                                | 4.69 ms: 1.02x slower                                                 |
| docutils       | 1.47 sec                                               | 1.47 sec: 1.00x slower                                                |
| html5lib       | 34.7 ms                                                | 35.8 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                                  |
| float          | 53.0 ms                                                | 56.1 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 75.4 ms: 1.02x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.59 ms: 1.02x faster                                                 |
| regex_dna      | 152 ms                                                 | 150 ms: 1.01x faster                                                  |
| regex_v8       | 16.1 ms                                                | 16.1 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.13 ms: 1.24x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 96.1 ms: 1.13x faster                                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 64.9 ms: 1.08x faster                                                 |
| unpickle_list        | 2.65 us                                                | 2.56 us: 1.04x faster                                                 |
| xml_etree_generate   | 48.3 ms                                                | 47.6 ms: 1.01x faster                                                 |
| xml_etree_process    | 35.1 ms                                                | 34.9 ms: 1.00x faster                                                 |
| json_loads           | 16.1 us                                                | 16.2 us: 1.01x slower                                                 |
| unpickle             | 9.67 us                                                | 9.75 us: 1.01x slower                                                 |
| pickle_list          | 2.81 us                                                | 2.85 us: 1.01x slower                                                 |
| unpickle_pure_python | 159 us                                                 | 162 us: 1.02x slower                                                  |
| pickle_pure_python   | 201 us                                                 | 205 us: 1.02x slower                                                  |
| pickle               | 7.15 us                                                | 7.55 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 7.16 ms: 1.42x faster                                                 |
| python_startup         | 12.4 ms                                                | 9.06 ms: 1.37x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.40x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 8.14 ms: 1.05x faster                                                 |
| genshi_text     | 15.3 ms                                                | 15.4 ms: 1.01x slower                                                 |
| genshi_xml      | 29.8 ms                                                | 30.3 ms: 1.02x slower                                                 |
| django_template | 21.0 ms                                                | 21.9 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site  | 10.2 ms                                                | 7.16 ms: 1.42x faster                                                 |
| python_startup          | 12.4 ms                                                | 9.06 ms: 1.37x faster                                                 |
| pathlib                 | 27.2 ms                                                | 20.6 ms: 1.33x faster                                                 |
| json_dumps              | 7.63 ms                                                | 6.13 ms: 1.24x faster                                                 |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.82 ms: 1.13x faster                                                 |
| xml_etree_parse         | 108 ms                                                 | 96.1 ms: 1.13x faster                                                 |
| coverage                | 58.4 ms                                                | 53.5 ms: 1.09x faster                                                 |
| flaskblogging           | 2.43 ms                                                | 2.23 ms: 1.09x faster                                                 |
| xml_etree_iterparse     | 70.1 ms                                                | 64.9 ms: 1.08x faster                                                 |
| mako                    | 8.53 ms                                                | 8.14 ms: 1.05x faster                                                 |
| bench_mp_pool           | 43.9 ms                                                | 41.9 ms: 1.05x faster                                                 |
| bench_thread_pool       | 474 us                                                 | 454 us: 1.04x faster                                                  |
| dulwich_log             | 30.3 ms                                                | 29.1 ms: 1.04x faster                                                 |
| unpickle_list           | 2.65 us                                                | 2.56 us: 1.04x faster                                                 |
| pylint                  | 272 ms                                                 | 265 ms: 1.03x faster                                                  |
| sqlalchemy_declarative  | 62.6 ms                                                | 61.2 ms: 1.02x faster                                                 |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.06 ms: 1.02x faster                                                 |
| regex_compile           | 76.7 ms                                                | 75.4 ms: 1.02x faster                                                 |
| regex_effbot            | 2.63 ms                                                | 2.59 ms: 1.02x faster                                                 |
| regex_dna               | 152 ms                                                 | 150 ms: 1.01x faster                                                  |
| telco                   | 3.41 ms                                                | 3.36 ms: 1.01x faster                                                 |
| scimark_lu              | 73.3 ms                                                | 72.3 ms: 1.01x faster                                                 |
| xml_etree_generate      | 48.3 ms                                                | 47.6 ms: 1.01x faster                                                 |
| mdp                     | 1.55 sec                                               | 1.53 sec: 1.01x faster                                                |
| async_tree_none         | 286 ms                                                 | 283 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed | 533 ms                                                 | 530 ms: 1.01x faster                                                  |
| scimark_fft             | 200 ms                                                 | 199 ms: 1.00x faster                                                  |
| xml_etree_process       | 35.1 ms                                                | 34.9 ms: 1.00x faster                                                 |
| regex_v8                | 16.1 ms                                                | 16.1 ms: 1.00x faster                                                 |
| docutils                | 1.47 sec                                               | 1.47 sec: 1.00x slower                                                |
| deltablue               | 2.81 ms                                                | 2.83 ms: 1.00x slower                                                 |
| pidigits                | 281 ms                                                 | 282 ms: 1.00x slower                                                  |
| sympy_sum               | 85.5 ms                                                | 85.9 ms: 1.00x slower                                                 |
| genshi_text             | 15.3 ms                                                | 15.4 ms: 1.01x slower                                                 |
| spectral_norm           | 72.6 ms                                                | 73.0 ms: 1.01x slower                                                 |
| json_loads              | 16.1 us                                                | 16.2 us: 1.01x slower                                                 |
| unpickle                | 9.67 us                                                | 9.75 us: 1.01x slower                                                 |
| sympy_integrate         | 11.5 ms                                                | 11.6 ms: 1.01x slower                                                 |
| thrift                  | 442 us                                                 | 446 us: 1.01x slower                                                  |
| crypto_pyaes            | 51.7 ms                                                | 52.2 ms: 1.01x slower                                                 |
| sympy_str               | 151 ms                                                 | 153 ms: 1.01x slower                                                  |
| pickle_list             | 2.81 us                                                | 2.85 us: 1.01x slower                                                 |
| genshi_xml              | 29.8 ms                                                | 30.3 ms: 1.02x slower                                                 |
| generators              | 28.8 ms                                                | 29.2 ms: 1.02x slower                                                 |
| unpickle_pure_python    | 159 us                                                 | 162 us: 1.02x slower                                                  |
| json                    | 2.78 ms                                                | 2.83 ms: 1.02x slower                                                 |
| chameleon               | 4.60 ms                                                | 4.69 ms: 1.02x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 174 ms: 1.02x slower                                                  |
| async_generators        | 196 ms                                                 | 201 ms: 1.02x slower                                                  |
| pycparser               | 698 ms                                                 | 713 ms: 1.02x slower                                                  |
| pickle_pure_python      | 201 us                                                 | 205 us: 1.02x slower                                                  |
| sympy_expand            | 242 ms                                                 | 248 ms: 1.03x slower                                                  |
| sqlglot_optimize        | 31.1 ms                                                | 31.9 ms: 1.03x slower                                                 |
| nqueens                 | 59.8 ms                                                | 61.3 ms: 1.03x slower                                                 |
| chaos                   | 49.4 ms                                                | 50.9 ms: 1.03x slower                                                 |
| html5lib                | 34.7 ms                                                | 35.8 ms: 1.03x slower                                                 |
| richards                | 32.2 ms                                                | 33.2 ms: 1.03x slower                                                 |
| fannkuch                | 261 ms                                                 | 270 ms: 1.03x slower                                                  |
| logging_simple          | 3.55 us                                                | 3.68 us: 1.04x slower                                                 |
| async_tree_io           | 704 ms                                                 | 732 ms: 1.04x slower                                                  |
| django_template         | 21.0 ms                                                | 21.9 ms: 1.04x slower                                                 |
| raytrace                | 207 ms                                                 | 216 ms: 1.04x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.17 ms: 1.04x slower                                                 |
| hexiom                  | 4.72 ms                                                | 4.93 ms: 1.04x slower                                                 |
| sqlglot_parse           | 959 us                                                 | 1.00 ms: 1.05x slower                                                 |
| logging_format          | 3.78 us                                                | 3.97 us: 1.05x slower                                                 |
| logging_silent          | 68.1 ns                                                | 71.7 ns: 1.05x slower                                                 |
| pprint_pformat          | 954 ms                                                 | 1.01 sec: 1.05x slower                                                |
| pickle                  | 7.15 us                                                | 7.55 us: 1.06x slower                                                 |
| float                   | 53.0 ms                                                | 56.1 ms: 1.06x slower                                                 |
| meteor_contest          | 73.5 ms                                                | 78.1 ms: 1.06x slower                                                 |
| pprint_safe_repr        | 466 ms                                                 | 496 ms: 1.06x slower                                                  |
| deepcopy                | 223 us                                                 | 240 us: 1.08x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.06 us: 1.08x slower                                                 |
| deepcopy_memo           | 26.3 us                                                | 28.5 us: 1.08x slower                                                 |
| go                      | 109 ms                                                 | 118 ms: 1.08x slower                                                  |
| coroutines              | 17.8 ms                                                | 19.5 ms: 1.10x slower                                                 |
| pyflate                 | 310 ms                                                 | 353 ms: 1.14x slower                                                  |
| async_tree_memoization  | 336 ms                                                 | 383 ms: 1.14x slower                                                  |
| 2to3                    | 161 ms                                                 | 185 ms: 1.15x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.46 us: 1.15x slower                                                 |
| scimark_monte_carlo     | 46.5 ms                                                | 55.4 ms: 1.19x slower                                                 |
| scimark_sor             | 82.6 ms                                                | 101 ms: 1.22x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (4): tornado_http, nbody, unpack_sequence, pickle_dict
Ignored benchmarks (11) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, gc_traversal, gunicorn, mypy2, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221002-3.12.0a0-14d4f68/bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68.json: mypy


# HPT report

- Reliability score: 97.27% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
