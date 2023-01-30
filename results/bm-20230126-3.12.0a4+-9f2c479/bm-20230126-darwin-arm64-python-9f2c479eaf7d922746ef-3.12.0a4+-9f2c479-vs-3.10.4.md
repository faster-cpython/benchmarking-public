
# Results vs. 3.10.4

- fork: python
- ref: 9f2c479eaf7d922746ef
- machine: darwin-arm64
- commit hash: 9f2c479
- commit date: 2023-01-26
- overall geometric mean: 1.23x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 222 ms                                                 | 185 ms: 1.20x faster                                                   |
| chameleon      | 5.86 ms                                                | 4.52 ms: 1.30x faster                                                  |
| docutils       | 1.76 sec                                               | 1.45 sec: 1.22x faster                                                 |
| html5lib       | 44.0 ms                                                | 35.1 ms: 1.25x faster                                                  |
| tornado_http   | 90.1 ms                                                | 71.2 ms: 1.27x faster                                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 94.6 ms                                                | 64.5 ms: 1.47x faster                                                  |
| float          | 72.1 ms                                                | 51.8 ms: 1.39x faster                                                  |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 96.2 ms                                                | 73.7 ms: 1.31x faster                                                  |
| regex_v8       | 17.7 ms                                                | 16.1 ms: 1.10x faster                                                  |
| regex_dna      | 164 ms                                                 | 153 ms: 1.08x faster                                                   |
| regex_effbot   | 2.45 ms                                                | 2.60 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 194 us: 1.46x faster                                                   |
| unpickle_pure_python | 204 us                                                 | 147 us: 1.39x faster                                                   |
| json_dumps           | 8.34 ms                                                | 6.23 ms: 1.34x faster                                                  |
| xml_etree_process    | 45.1 ms                                                | 35.6 ms: 1.27x faster                                                  |
| xml_etree_generate   | 54.5 ms                                                | 49.3 ms: 1.11x faster                                                  |
| xml_etree_parse      | 100 ms                                                 | 93.7 ms: 1.07x faster                                                  |
| json_loads           | 17.0 us                                                | 16.2 us: 1.05x faster                                                  |
| xml_etree_iterparse  | 69.0 ms                                                | 67.7 ms: 1.02x faster                                                  |
| unpickle             | 10.0 us                                                | 9.89 us: 1.01x faster                                                  |
| pickle               | 7.50 us                                                | 7.56 us: 1.01x slower                                                  |
| unpickle_list        | 2.66 us                                                | 2.77 us: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                           |

Benchmark hidden because not significant (2): pickle_dict, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 9.59 ms                                                | 9.40 ms: 1.02x faster                                                  |
| python_startup_no_site | 7.00 ms                                                | 7.39 ms: 1.06x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.6 ms                                                | 7.27 ms: 1.46x faster                                                  |
| genshi_xml      | 37.7 ms                                                | 28.9 ms: 1.31x faster                                                  |
| django_template | 27.2 ms                                                | 21.3 ms: 1.28x faster                                                  |
| genshi_text     | 18.2 ms                                                | 14.7 ms: 1.24x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 5.37 ms                                                | 2.50 ms: 2.15x faster                                                  |
| logging_silent          | 119 ns                                                 | 66.3 ns: 1.80x faster                                                  |
| richards                | 51.4 ms                                                | 31.1 ms: 1.65x faster                                                  |
| scimark_sor             | 126 ms                                                 | 78.3 ms: 1.61x faster                                                  |
| scimark_lu              | 110 ms                                                 | 71.0 ms: 1.55x faster                                                  |
| raytrace                | 329 ms                                                 | 216 ms: 1.52x faster                                                   |
| crypto_pyaes            | 77.9 ms                                                | 51.9 ms: 1.50x faster                                                  |
| async_tree_memoization  | 485 ms                                                 | 324 ms: 1.50x faster                                                   |
| go                      | 165 ms                                                 | 110 ms: 1.49x faster                                                   |
| nbody                   | 94.6 ms                                                | 64.5 ms: 1.47x faster                                                  |
| pickle_pure_python      | 284 us                                                 | 194 us: 1.46x faster                                                   |
| mako                    | 10.6 ms                                                | 7.27 ms: 1.46x faster                                                  |
| scimark_monte_carlo     | 72.3 ms                                                | 50.4 ms: 1.44x faster                                                  |
| pyflate                 | 454 ms                                                 | 324 ms: 1.40x faster                                                   |
| chaos                   | 66.5 ms                                                | 47.8 ms: 1.39x faster                                                  |
| float                   | 72.1 ms                                                | 51.8 ms: 1.39x faster                                                  |
| unpickle_pure_python    | 204 us                                                 | 147 us: 1.39x faster                                                   |
| async_tree_none         | 396 ms                                                 | 288 ms: 1.37x faster                                                   |
| async_tree_io           | 1.01 sec                                               | 742 ms: 1.36x faster                                                   |
| pycparser               | 915 ms                                                 | 680 ms: 1.35x faster                                                   |
| json_dumps              | 8.34 ms                                                | 6.23 ms: 1.34x faster                                                  |
| hexiom                  | 6.31 ms                                                | 4.73 ms: 1.34x faster                                                  |
| spectral_norm           | 95.8 ms                                                | 72.3 ms: 1.33x faster                                                  |
| deepcopy_memo           | 34.4 us                                                | 26.0 us: 1.32x faster                                                  |
| pprint_pformat          | 1.24 sec                                               | 946 ms: 1.31x faster                                                   |
| sqlglot_parse           | 1.33 ms                                                | 1.01 ms: 1.31x faster                                                  |
| sqlglot_transpile       | 1.54 ms                                                | 1.18 ms: 1.31x faster                                                  |
| genshi_xml              | 37.7 ms                                                | 28.9 ms: 1.31x faster                                                  |
| logging_simple          | 4.61 us                                                | 3.53 us: 1.31x faster                                                  |
| regex_compile           | 96.2 ms                                                | 73.7 ms: 1.31x faster                                                  |
| pprint_safe_repr        | 608 ms                                                 | 465 ms: 1.31x faster                                                   |
| thrift                  | 577 us                                                 | 443 us: 1.30x faster                                                   |
| logging_format          | 4.95 us                                                | 3.80 us: 1.30x faster                                                  |
| chameleon               | 5.86 ms                                                | 4.52 ms: 1.30x faster                                                  |
| django_template         | 27.2 ms                                                | 21.3 ms: 1.28x faster                                                  |
| dulwich_log             | 36.4 ms                                                | 28.5 ms: 1.28x faster                                                  |
| deepcopy                | 278 us                                                 | 219 us: 1.27x faster                                                   |
| tornado_http            | 90.1 ms                                                | 71.2 ms: 1.27x faster                                                  |
| xml_etree_process       | 45.1 ms                                                | 35.6 ms: 1.27x faster                                                  |
| mypy                    | 521 ms                                                 | 414 ms: 1.26x faster                                                   |
| html5lib                | 44.0 ms                                                | 35.1 ms: 1.25x faster                                                  |
| fannkuch                | 318 ms                                                 | 256 ms: 1.24x faster                                                   |
| genshi_text             | 18.2 ms                                                | 14.7 ms: 1.24x faster                                                  |
| deepcopy_reduce         | 2.36 us                                                | 1.92 us: 1.23x faster                                                  |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.82 ms: 1.23x faster                                                  |
| async_tree_cpu_io_mixed | 665 ms                                                 | 544 ms: 1.22x faster                                                   |
| docutils                | 1.76 sec                                               | 1.45 sec: 1.22x faster                                                 |
| sqlglot_optimize        | 38.1 ms                                                | 31.4 ms: 1.21x faster                                                  |
| 2to3                    | 222 ms                                                 | 185 ms: 1.20x faster                                                   |
| scimark_fft             | 231 ms                                                 | 193 ms: 1.20x faster                                                   |
| sympy_integrate         | 13.3 ms                                                | 11.1 ms: 1.19x faster                                                  |
| bench_thread_pool       | 531 us                                                 | 450 us: 1.18x faster                                                   |
| sympy_str               | 169 ms                                                 | 145 ms: 1.17x faster                                                   |
| unpack_sequence         | 38.2 ns                                                | 32.7 ns: 1.17x faster                                                  |
| async_generators        | 231 ms                                                 | 199 ms: 1.16x faster                                                   |
| sqlglot_normalize       | 198 ms                                                 | 172 ms: 1.15x faster                                                   |
| nqueens                 | 68.6 ms                                                | 59.7 ms: 1.15x faster                                                  |
| sympy_sum               | 93.5 ms                                                | 81.4 ms: 1.15x faster                                                  |
| sympy_expand            | 275 ms                                                 | 240 ms: 1.15x faster                                                   |
| xml_etree_generate      | 54.5 ms                                                | 49.3 ms: 1.11x faster                                                  |
| sqlite_synth            | 1.50 us                                                | 1.36 us: 1.10x faster                                                  |
| regex_v8                | 17.7 ms                                                | 16.1 ms: 1.10x faster                                                  |
| json                    | 3.13 ms                                                | 2.84 ms: 1.10x faster                                                  |
| mdp                     | 1.66 sec                                               | 1.51 sec: 1.10x faster                                                 |
| regex_dna               | 164 ms                                                 | 153 ms: 1.08x faster                                                   |
| pathlib                 | 22.2 ms                                                | 20.7 ms: 1.07x faster                                                  |
| telco                   | 3.63 ms                                                | 3.39 ms: 1.07x faster                                                  |
| xml_etree_parse         | 100 ms                                                 | 93.7 ms: 1.07x faster                                                  |
| coroutines              | 20.1 ms                                                | 18.8 ms: 1.07x faster                                                  |
| meteor_contest          | 77.7 ms                                                | 73.8 ms: 1.05x faster                                                  |
| json_loads              | 17.0 us                                                | 16.2 us: 1.05x faster                                                  |
| python_startup          | 9.59 ms                                                | 9.40 ms: 1.02x faster                                                  |
| xml_etree_iterparse     | 69.0 ms                                                | 67.7 ms: 1.02x faster                                                  |
| unpickle                | 10.0 us                                                | 9.89 us: 1.01x faster                                                  |
| pidigits                | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| pickle                  | 7.50 us                                                | 7.56 us: 1.01x slower                                                  |
| unpickle_list           | 2.66 us                                                | 2.77 us: 1.04x slower                                                  |
| python_startup_no_site  | 7.00 ms                                                | 7.39 ms: 1.06x slower                                                  |
| bench_mp_pool           | 40.8 ms                                                | 43.3 ms: 1.06x slower                                                  |
| regex_effbot            | 2.45 ms                                                | 2.60 ms: 1.06x slower                                                  |
| generators              | 32.5 ms                                                | 34.6 ms: 1.06x slower                                                  |
| coverage                | 40.8 ms                                                | 56.9 ms: 1.40x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (2): pickle_dict, pickle_list
Ignored benchmarks (6) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20230126-3.12.0a4+-9f2c479/bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479.json: asyncio_tcp, create_gc_cycles, dask, gc_traversal
