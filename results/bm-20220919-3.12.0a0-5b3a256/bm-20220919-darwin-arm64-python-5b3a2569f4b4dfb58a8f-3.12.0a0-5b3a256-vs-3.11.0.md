
# Results vs. 3.11.0

- fork: python
- ref: 5b3a2569f4b4dfb58a8f
- machine: darwin-arm64
- commit hash: 5b3a256
- commit date: 2022-09-19
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 181 ms                                                              | 185 ms: 1.02x slower                                                  |
| chameleon      | 4.61 ms                                                             | 4.69 ms: 1.02x slower                                                 |
| docutils       | 1.46 sec                                                            | 1.48 sec: 1.01x slower                                                |
| html5lib       | 34.7 ms                                                             | 35.8 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                               | 1.01x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 51.7 ms                                                             | 55.9 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                               | 1.03x slower                                                          |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 76.3 ms                                                             | 75.6 ms: 1.01x faster                                                 |
| regex_effbot   | 2.63 ms                                                             | 2.67 ms: 1.02x slower                                                 |
| regex_v8       | 16.5 ms                                                             | 16.7 ms: 1.02x slower                                                 |
| regex_dna      | 151 ms                                                              | 155 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                               | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 7.67 ms                                                             | 6.09 ms: 1.26x faster                                                 |
| unpickle_list        | 2.64 us                                                             | 2.54 us: 1.04x faster                                                 |
| xml_etree_parse      | 99.6 ms                                                             | 96.1 ms: 1.04x faster                                                 |
| xml_etree_generate   | 48.4 ms                                                             | 47.5 ms: 1.02x faster                                                 |
| xml_etree_iterparse  | 65.6 ms                                                             | 64.8 ms: 1.01x faster                                                 |
| pickle_list          | 2.86 us                                                             | 2.83 us: 1.01x faster                                                 |
| xml_etree_process    | 35.1 ms                                                             | 34.9 ms: 1.00x faster                                                 |
| pickle_dict          | 17.9 us                                                             | 17.9 us: 1.00x faster                                                 |
| unpickle_pure_python | 159 us                                                              | 161 us: 1.01x slower                                                  |
| pickle_pure_python   | 200 us                                                              | 206 us: 1.03x slower                                                  |
| pickle               | 7.21 us                                                             | 7.52 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                               | 1.02x faster                                                          |

Benchmark hidden because not significant (2): json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 9.19 ms                                                             | 9.22 ms: 1.00x slower                                                 |
| python_startup_no_site | 7.24 ms                                                             | 7.30 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                               | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.40 ms                                                             | 8.14 ms: 1.03x faster                                                 |
| genshi_xml      | 30.5 ms                                                             | 30.1 ms: 1.01x faster                                                 |
| django_template | 21.1 ms                                                             | 21.8 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                               | 1.00x faster                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps              | 7.67 ms                                                             | 6.09 ms: 1.26x faster                                                 |
| scimark_sparse_mat_mult | 3.20 ms                                                             | 2.83 ms: 1.13x faster                                                 |
| coverage                | 58.4 ms                                                             | 53.3 ms: 1.09x faster                                                 |
| unpickle_list           | 2.64 us                                                             | 2.54 us: 1.04x faster                                                 |
| xml_etree_parse         | 99.6 ms                                                             | 96.1 ms: 1.04x faster                                                 |
| mako                    | 8.40 ms                                                             | 8.14 ms: 1.03x faster                                                 |
| flaskblogging           | 2.29 ms                                                             | 2.24 ms: 1.02x faster                                                 |
| sqlalchemy_imperative   | 7.22 ms                                                             | 7.07 ms: 1.02x faster                                                 |
| sqlalchemy_declarative  | 62.4 ms                                                             | 61.3 ms: 1.02x faster                                                 |
| xml_etree_generate      | 48.4 ms                                                             | 47.5 ms: 1.02x faster                                                 |
| logging_silent          | 67.4 ns                                                             | 66.5 ns: 1.01x faster                                                 |
| mypy                    | 421 ms                                                              | 415 ms: 1.01x faster                                                  |
| genshi_xml              | 30.5 ms                                                             | 30.1 ms: 1.01x faster                                                 |
| xml_etree_iterparse     | 65.6 ms                                                             | 64.8 ms: 1.01x faster                                                 |
| pickle_list             | 2.86 us                                                             | 2.83 us: 1.01x faster                                                 |
| regex_compile           | 76.3 ms                                                             | 75.6 ms: 1.01x faster                                                 |
| telco                   | 3.39 ms                                                             | 3.36 ms: 1.01x faster                                                 |
| mdp                     | 1.54 sec                                                            | 1.53 sec: 1.01x faster                                                |
| scimark_fft             | 201 ms                                                              | 199 ms: 1.01x faster                                                  |
| bench_thread_pool       | 457 us                                                              | 455 us: 1.01x faster                                                  |
| xml_etree_process       | 35.1 ms                                                             | 34.9 ms: 1.00x faster                                                 |
| pickle_dict             | 17.9 us                                                             | 17.9 us: 1.00x faster                                                 |
| spectral_norm           | 72.7 ms                                                             | 72.9 ms: 1.00x slower                                                 |
| python_startup          | 9.19 ms                                                             | 9.22 ms: 1.00x slower                                                 |
| scimark_lu              | 72.2 ms                                                             | 72.4 ms: 1.00x slower                                                 |
| dulwich_log             | 29.1 ms                                                             | 29.1 ms: 1.00x slower                                                 |
| deltablue               | 2.82 ms                                                             | 2.83 ms: 1.00x slower                                                 |
| crypto_pyaes            | 51.7 ms                                                             | 52.0 ms: 1.01x slower                                                 |
| sympy_sum               | 85.5 ms                                                             | 86.1 ms: 1.01x slower                                                 |
| python_startup_no_site  | 7.24 ms                                                             | 7.30 ms: 1.01x slower                                                 |
| unpickle_pure_python    | 159 us                                                              | 161 us: 1.01x slower                                                  |
| docutils                | 1.46 sec                                                            | 1.48 sec: 1.01x slower                                                |
| sympy_integrate         | 11.5 ms                                                             | 11.7 ms: 1.01x slower                                                 |
| regex_effbot            | 2.63 ms                                                             | 2.67 ms: 1.02x slower                                                 |
| regex_v8                | 16.5 ms                                                             | 16.7 ms: 1.02x slower                                                 |
| chameleon               | 4.61 ms                                                             | 4.69 ms: 1.02x slower                                                 |
| sqlglot_optimize        | 31.3 ms                                                             | 31.9 ms: 1.02x slower                                                 |
| richards                | 32.7 ms                                                             | 33.3 ms: 1.02x slower                                                 |
| sqlglot_normalize       | 171 ms                                                              | 174 ms: 1.02x slower                                                  |
| sympy_str               | 151 ms                                                              | 154 ms: 1.02x slower                                                  |
| 2to3                    | 181 ms                                                              | 185 ms: 1.02x slower                                                  |
| regex_dna               | 151 ms                                                              | 155 ms: 1.02x slower                                                  |
| sympy_expand            | 242 ms                                                              | 248 ms: 1.03x slower                                                  |
| chaos                   | 49.3 ms                                                             | 50.7 ms: 1.03x slower                                                 |
| pycparser               | 694 ms                                                              | 713 ms: 1.03x slower                                                  |
| generators              | 28.4 ms                                                             | 29.2 ms: 1.03x slower                                                 |
| nqueens                 | 59.5 ms                                                             | 61.2 ms: 1.03x slower                                                 |
| async_generators        | 195 ms                                                              | 201 ms: 1.03x slower                                                  |
| thrift                  | 429 us                                                              | 443 us: 1.03x slower                                                  |
| pickle_pure_python      | 200 us                                                              | 206 us: 1.03x slower                                                  |
| unpack_sequence         | 33.1 ns                                                             | 34.2 ns: 1.03x slower                                                 |
| html5lib                | 34.7 ms                                                             | 35.8 ms: 1.03x slower                                                 |
| fannkuch                | 262 ms                                                              | 272 ms: 1.04x slower                                                  |
| raytrace                | 207 ms                                                              | 215 ms: 1.04x slower                                                  |
| django_template         | 21.1 ms                                                             | 21.8 ms: 1.04x slower                                                 |
| hexiom                  | 4.73 ms                                                             | 4.92 ms: 1.04x slower                                                 |
| pickle                  | 7.21 us                                                             | 7.52 us: 1.04x slower                                                 |
| sqlglot_transpile       | 1.11 ms                                                             | 1.17 ms: 1.05x slower                                                 |
| async_tree_io           | 696 ms                                                              | 732 ms: 1.05x slower                                                  |
| logging_simple          | 3.47 us                                                             | 3.65 us: 1.05x slower                                                 |
| meteor_contest          | 73.9 ms                                                             | 77.9 ms: 1.05x slower                                                 |
| sqlglot_parse           | 948 us                                                              | 1.00 ms: 1.06x slower                                                 |
| logging_format          | 3.73 us                                                             | 3.94 us: 1.06x slower                                                 |
| pprint_pformat          | 953 ms                                                              | 1.01 sec: 1.06x slower                                                |
| pprint_safe_repr        | 467 ms                                                              | 496 ms: 1.06x slower                                                  |
| go                      | 109 ms                                                              | 118 ms: 1.08x slower                                                  |
| deepcopy                | 222 us                                                              | 240 us: 1.08x slower                                                  |
| float                   | 51.7 ms                                                             | 55.9 ms: 1.08x slower                                                 |
| deepcopy_reduce         | 1.90 us                                                             | 2.07 us: 1.09x slower                                                 |
| deepcopy_memo           | 26.2 us                                                             | 28.7 us: 1.10x slower                                                 |
| coroutines              | 17.8 ms                                                             | 19.5 ms: 1.10x slower                                                 |
| pyflate                 | 313 ms                                                              | 350 ms: 1.12x slower                                                  |
| sqlite_synth            | 1.29 us                                                             | 1.45 us: 1.12x slower                                                 |
| scimark_monte_carlo     | 46.9 ms                                                             | 54.4 ms: 1.16x slower                                                 |
| async_tree_memoization  | 317 ms                                                              | 381 ms: 1.20x slower                                                  |
| scimark_sor             | 83.3 ms                                                             | 101 ms: 1.22x slower                                                  |
| Geometric mean          | (ref)                                                               | 1.02x slower                                                          |

Benchmark hidden because not significant (12): tornado_http, pylint, pathlib, genshi_text, json_loads, unpickle, bench_mp_pool, pidigits, async_tree_cpu_io_mixed, nbody, json, async_tree_none
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, gunicorn
