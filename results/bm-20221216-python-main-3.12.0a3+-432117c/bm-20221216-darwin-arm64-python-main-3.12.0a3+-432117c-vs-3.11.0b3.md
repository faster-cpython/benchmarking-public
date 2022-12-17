Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220601-darwin-arm64-python-eb0004c27163ec089201-3.11.0b3-eb0004c | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 182 ms                                                                | 184 ms: 1.01x slower                                   |
| chameleon      | 4.73 ms                                                               | 4.29 ms: 1.10x faster                                  |
| docutils       | 1.46 sec                                                              | 1.44 sec: 1.02x faster                                 |
| html5lib       | 35.8 ms                                                               | 33.2 ms: 1.08x faster                                  |
| Geometric mean | (ref)                                                                 | 1.05x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220601-darwin-arm64-python-eb0004c27163ec089201-3.11.0b3-eb0004c | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------:|
| float          | 55.7 ms                                                               | 53.4 ms: 1.04x faster                                  |
| nbody          | 63.8 ms                                                               | 62.3 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                                 | 1.02x faster                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220601-darwin-arm64-python-eb0004c27163ec089201-3.11.0b3-eb0004c | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 77.7 ms                                                               | 72.7 ms: 1.07x faster                                  |
| regex_effbot   | 2.40 ms                                                               | 2.71 ms: 1.13x slower                                  |
| regex_v8       | 16.8 ms                                                               | 16.0 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220601-darwin-arm64-python-eb0004c27163ec089201-3.11.0b3-eb0004c | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.69 ms                                                               | 6.16 ms: 1.25x faster                                  |
| json_loads           | 16.4 us                                                               | 16.3 us: 1.01x faster                                  |
| pickle               | 7.14 us                                                               | 7.55 us: 1.06x slower                                  |
| pickle_dict          | 17.6 us                                                               | 18.0 us: 1.02x slower                                  |
| pickle_list          | 2.73 us                                                               | 2.84 us: 1.04x slower                                  |
| pickle_pure_python   | 222 us                                                                | 197 us: 1.12x faster                                   |
| unpickle             | 9.97 us                                                               | 9.84 us: 1.01x faster                                  |
| unpickle_list        | 2.77 us                                                               | 2.56 us: 1.08x faster                                  |
| unpickle_pure_python | 175 us                                                                | 151 us: 1.16x faster                                   |
| xml_etree_parse      | 99.1 ms                                                               | 92.9 ms: 1.07x faster                                  |
| xml_etree_iterparse  | 65.2 ms                                                               | 65.5 ms: 1.00x slower                                  |
| xml_etree_generate   | 48.0 ms                                                               | 47.0 ms: 1.02x faster                                  |
| xml_etree_process    | 34.8 ms                                                               | 34.4 ms: 1.01x faster                                  |
| Geometric mean       | (ref)                                                                 | 1.04x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220601-darwin-arm64-python-eb0004c27163ec089201-3.11.0b3-eb0004c | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 9.25 ms                                                               | 9.29 ms: 1.00x slower                                  |
| python_startup_no_site | 7.30 ms                                                               | 7.34 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220601-darwin-arm64-python-eb0004c27163ec089201-3.11.0b3-eb0004c | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 21.0 ms                                                               | 20.7 ms: 1.02x faster                                  |
| genshi_text     | 15.5 ms                                                               | 13.9 ms: 1.12x faster                                  |
| genshi_xml      | 31.3 ms                                                               | 28.2 ms: 1.11x faster                                  |
| mako            | 8.44 ms                                                               | 6.96 ms: 1.21x faster                                  |
| Geometric mean  | (ref)                                                                 | 1.11x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220601-darwin-arm64-python-eb0004c27163ec089201-3.11.0b3-eb0004c | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------:|
| 2to3                    | 182 ms                                                                | 184 ms: 1.01x slower                                   |
| async_generators        | 197 ms                                                                | 201 ms: 1.02x slower                                   |
| async_tree_none         | 287 ms                                                                | 285 ms: 1.01x faster                                   |
| async_tree_cpu_io_mixed | 533 ms                                                                | 538 ms: 1.01x slower                                   |
| async_tree_io           | 702 ms                                                                | 732 ms: 1.04x slower                                   |
| async_tree_memoization  | 346 ms                                                                | 330 ms: 1.05x faster                                   |
| chameleon               | 4.73 ms                                                               | 4.29 ms: 1.10x faster                                  |
| chaos                   | 49.5 ms                                                               | 48.6 ms: 1.02x faster                                  |
| bench_mp_pool           | 41.0 ms                                                               | 43.9 ms: 1.07x slower                                  |
| bench_thread_pool       | 462 us                                                                | 445 us: 1.04x faster                                   |
| coroutines              | 17.4 ms                                                               | 17.4 ms: 1.00x slower                                  |
| crypto_pyaes            | 51.7 ms                                                               | 53.0 ms: 1.03x slower                                  |
| deepcopy                | 237 us                                                                | 227 us: 1.04x faster                                   |
| deepcopy_reduce         | 2.04 us                                                               | 1.95 us: 1.04x faster                                  |
| deepcopy_memo           | 28.7 us                                                               | 27.4 us: 1.05x faster                                  |
| deltablue               | 2.83 ms                                                               | 2.51 ms: 1.13x faster                                  |
| django_template         | 21.0 ms                                                               | 20.7 ms: 1.02x faster                                  |
| docutils                | 1.46 sec                                                              | 1.44 sec: 1.02x faster                                 |
| dulwich_log             | 29.4 ms                                                               | 28.4 ms: 1.04x faster                                  |
| fannkuch                | 261 ms                                                                | 255 ms: 1.02x faster                                   |
| float                   | 55.7 ms                                                               | 53.4 ms: 1.04x faster                                  |
| generators              | 27.7 ms                                                               | 32.2 ms: 1.16x slower                                  |
| genshi_text             | 15.5 ms                                                               | 13.9 ms: 1.12x faster                                  |
| genshi_xml              | 31.3 ms                                                               | 28.2 ms: 1.11x faster                                  |
| go                      | 106 ms                                                                | 106 ms: 1.00x faster                                   |
| hexiom                  | 4.71 ms                                                               | 4.59 ms: 1.02x faster                                  |
| html5lib                | 35.8 ms                                                               | 33.2 ms: 1.08x faster                                  |
| json                    | 2.91 ms                                                               | 2.82 ms: 1.03x faster                                  |
| json_dumps              | 7.69 ms                                                               | 6.16 ms: 1.25x faster                                  |
| json_loads              | 16.4 us                                                               | 16.3 us: 1.01x faster                                  |
| logging_silent          | 65.7 ns                                                               | 62.7 ns: 1.05x faster                                  |
| mako                    | 8.44 ms                                                               | 6.96 ms: 1.21x faster                                  |
| mdp                     | 1.53 sec                                                              | 1.50 sec: 1.02x faster                                 |
| meteor_contest          | 77.8 ms                                                               | 75.4 ms: 1.03x faster                                  |
| mypy                    | 418 ms                                                                | 410 ms: 1.02x faster                                   |
| nbody                   | 63.8 ms                                                               | 62.3 ms: 1.02x faster                                  |
| nqueens                 | 58.7 ms                                                               | 59.3 ms: 1.01x slower                                  |
| pathlib                 | 20.8 ms                                                               | 20.4 ms: 1.02x faster                                  |
| pickle                  | 7.14 us                                                               | 7.55 us: 1.06x slower                                  |
| pickle_dict             | 17.6 us                                                               | 18.0 us: 1.02x slower                                  |
| pickle_list             | 2.73 us                                                               | 2.84 us: 1.04x slower                                  |
| pickle_pure_python      | 222 us                                                                | 197 us: 1.12x faster                                   |
| pprint_safe_repr        | 488 ms                                                                | 470 ms: 1.04x faster                                   |
| pprint_pformat          | 1.00 sec                                                              | 955 ms: 1.05x faster                                   |
| pycparser               | 704 ms                                                                | 665 ms: 1.06x faster                                   |
| pyflate                 | 318 ms                                                                | 324 ms: 1.02x slower                                   |
| python_startup          | 9.25 ms                                                               | 9.29 ms: 1.00x slower                                  |
| python_startup_no_site  | 7.30 ms                                                               | 7.34 ms: 1.01x slower                                  |
| raytrace                | 208 ms                                                                | 203 ms: 1.02x faster                                   |
| regex_compile           | 77.7 ms                                                               | 72.7 ms: 1.07x faster                                  |
| regex_effbot            | 2.40 ms                                                               | 2.71 ms: 1.13x slower                                  |
| regex_v8                | 16.8 ms                                                               | 16.0 ms: 1.05x faster                                  |
| richards                | 33.3 ms                                                               | 29.2 ms: 1.14x faster                                  |
| scimark_fft             | 199 ms                                                                | 193 ms: 1.03x faster                                   |
| scimark_lu              | 71.8 ms                                                               | 69.0 ms: 1.04x faster                                  |
| scimark_monte_carlo     | 48.9 ms                                                               | 46.1 ms: 1.06x faster                                  |
| scimark_sor             | 77.6 ms                                                               | 78.1 ms: 1.01x slower                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                               | 2.77 ms: 1.16x faster                                  |
| spectral_norm           | 72.2 ms                                                               | 71.7 ms: 1.01x faster                                  |
| sqlglot_parse           | 1.19 ms                                                               | 976 us: 1.22x faster                                   |
| sqlglot_transpile       | 1.35 ms                                                               | 1.14 ms: 1.19x faster                                  |
| sqlglot_optimize        | 31.4 ms                                                               | 30.8 ms: 1.02x faster                                  |
| sqlglot_normalize       | 169 ms                                                                | 167 ms: 1.01x faster                                   |
| sqlite_synth            | 1.35 us                                                               | 1.43 us: 1.06x slower                                  |
| sympy_expand            | 243 ms                                                                | 240 ms: 1.01x faster                                   |
| sympy_integrate         | 11.6 ms                                                               | 11.3 ms: 1.02x faster                                  |
| sympy_sum               | 82.4 ms                                                               | 85.0 ms: 1.03x slower                                  |
| sympy_str               | 151 ms                                                                | 150 ms: 1.01x faster                                   |
| telco                   | 3.42 ms                                                               | 3.35 ms: 1.02x faster                                  |
| thrift                  | 435 us                                                                | 433 us: 1.01x faster                                   |
| unpack_sequence         | 32.2 ns                                                               | 30.4 ns: 1.06x faster                                  |
| unpickle                | 9.97 us                                                               | 9.84 us: 1.01x faster                                  |
| unpickle_list           | 2.77 us                                                               | 2.56 us: 1.08x faster                                  |
| unpickle_pure_python    | 175 us                                                                | 151 us: 1.16x faster                                   |
| xml_etree_parse         | 99.1 ms                                                               | 92.9 ms: 1.07x faster                                  |
| xml_etree_iterparse     | 65.2 ms                                                               | 65.5 ms: 1.00x slower                                  |
| xml_etree_generate      | 48.0 ms                                                               | 47.0 ms: 1.02x faster                                  |
| xml_etree_process       | 34.8 ms                                                               | 34.4 ms: 1.01x faster                                  |
| Geometric mean          | (ref)                                                                 | 1.03x faster                                           |

Benchmark hidden because not significant (4): logging_format, logging_simple, pidigits, regex_dna
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220601-python-eb0004c27163ec089201-3.11.0b3-eb0004c/bm-20220601-darwin-arm64-python-eb0004c27163ec089201-3.11.0b3-eb0004c.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221216-python-main-3.12.0a3+-432117c/bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c.json: coverage
