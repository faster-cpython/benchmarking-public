
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
| 2to3           | 201 ms                                                 | 185 ms: 1.09x faster                                                   |
| chameleon      | 5.79 ms                                                | 4.52 ms: 1.28x faster                                                  |
| docutils       | 1.78 sec                                               | 1.45 sec: 1.23x faster                                                 |
| html5lib       | 44.2 ms                                                | 35.1 ms: 1.26x faster                                                  |
| tornado_http   | 91.5 ms                                                | 71.2 ms: 1.29x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 64.5 ms: 1.45x faster                                                  |
| float          | 72.4 ms                                                | 51.8 ms: 1.40x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 73.7 ms: 1.31x faster                                                  |
| regex_v8       | 17.6 ms                                                | 16.1 ms: 1.09x faster                                                  |
| regex_dna      | 162 ms                                                 | 153 ms: 1.06x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.60 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 194 us: 1.46x faster                                                   |
| unpickle_pure_python | 203 us                                                 | 147 us: 1.38x faster                                                   |
| json_dumps           | 8.40 ms                                                | 6.23 ms: 1.35x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 35.6 ms: 1.26x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 93.7 ms: 1.14x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 49.3 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 67.7 ms: 1.07x faster                                                  |
| json_loads           | 16.9 us                                                | 16.2 us: 1.04x faster                                                  |
| pickle_dict          | 17.9 us                                                | 17.9 us: 1.00x slower                                                  |
| pickle_list          | 2.80 us                                                | 2.83 us: 1.01x slower                                                  |
| pickle               | 7.35 us                                                | 7.56 us: 1.03x slower                                                  |
| unpickle_list        | 2.69 us                                                | 2.77 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.40 ms: 1.27x faster                                                  |
| python_startup_no_site | 8.88 ms                                                | 7.39 ms: 1.20x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.27 ms: 1.44x faster                                                  |
| genshi_xml      | 37.2 ms                                                | 28.9 ms: 1.29x faster                                                  |
| django_template | 27.3 ms                                                | 21.3 ms: 1.28x faster                                                  |
| genshi_text     | 18.4 ms                                                | 14.7 ms: 1.25x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.50 ms: 2.06x faster                                                  |
| logging_silent          | 119 ns                                                 | 66.3 ns: 1.80x faster                                                  |
| richards                | 51.4 ms                                                | 31.1 ms: 1.65x faster                                                  |
| scimark_sor             | 126 ms                                                 | 78.3 ms: 1.61x faster                                                  |
| scimark_lu              | 109 ms                                                 | 71.0 ms: 1.54x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 324 ms: 1.51x faster                                                   |
| crypto_pyaes            | 78.1 ms                                                | 51.9 ms: 1.50x faster                                                  |
| raytrace                | 325 ms                                                 | 216 ms: 1.50x faster                                                   |
| asyncio_tcp             | 670 ms                                                 | 446 ms: 1.50x faster                                                   |
| go                      | 165 ms                                                 | 110 ms: 1.50x faster                                                   |
| pickle_pure_python      | 283 us                                                 | 194 us: 1.46x faster                                                   |
| nbody                   | 93.3 ms                                                | 64.5 ms: 1.45x faster                                                  |
| mako                    | 10.5 ms                                                | 7.27 ms: 1.44x faster                                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 50.4 ms: 1.44x faster                                                  |
| pyflate                 | 453 ms                                                 | 324 ms: 1.40x faster                                                   |
| float                   | 72.4 ms                                                | 51.8 ms: 1.40x faster                                                  |
| chaos                   | 66.7 ms                                                | 47.8 ms: 1.40x faster                                                  |
| async_tree_none         | 400 ms                                                 | 288 ms: 1.39x faster                                                   |
| pathlib                 | 28.8 ms                                                | 20.7 ms: 1.39x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 147 us: 1.38x faster                                                   |
| async_tree_io           | 1.02 sec                                               | 742 ms: 1.37x faster                                                   |
| json_dumps              | 8.40 ms                                                | 6.23 ms: 1.35x faster                                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.01 ms: 1.35x faster                                                  |
| pycparser               | 916 ms                                                 | 680 ms: 1.35x faster                                                   |
| hexiom                  | 6.32 ms                                                | 4.73 ms: 1.34x faster                                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.18 ms: 1.34x faster                                                  |
| spectral_norm           | 95.8 ms                                                | 72.3 ms: 1.33x faster                                                  |
| deepcopy_memo           | 34.4 us                                                | 26.0 us: 1.32x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.53 us: 1.31x faster                                                  |
| thrift                  | 580 us                                                 | 443 us: 1.31x faster                                                   |
| regex_compile           | 96.4 ms                                                | 73.7 ms: 1.31x faster                                                  |
| logging_format          | 4.97 us                                                | 3.80 us: 1.31x faster                                                  |
| pprint_pformat          | 1.23 sec                                               | 946 ms: 1.30x faster                                                   |
| pprint_safe_repr        | 606 ms                                                 | 465 ms: 1.30x faster                                                   |
| dulwich_log             | 37.1 ms                                                | 28.5 ms: 1.30x faster                                                  |
| genshi_xml              | 37.2 ms                                                | 28.9 ms: 1.29x faster                                                  |
| deepcopy                | 281 us                                                 | 219 us: 1.29x faster                                                   |
| tornado_http            | 91.5 ms                                                | 71.2 ms: 1.29x faster                                                  |
| chameleon               | 5.79 ms                                                | 4.52 ms: 1.28x faster                                                  |
| django_template         | 27.3 ms                                                | 21.3 ms: 1.28x faster                                                  |
| create_gc_cycles        | 880 us                                                 | 692 us: 1.27x faster                                                   |
| python_startup          | 11.9 ms                                                | 9.40 ms: 1.27x faster                                                  |
| html5lib                | 44.2 ms                                                | 35.1 ms: 1.26x faster                                                  |
| xml_etree_process       | 44.8 ms                                                | 35.6 ms: 1.26x faster                                                  |
| genshi_text             | 18.4 ms                                                | 14.7 ms: 1.25x faster                                                  |
| fannkuch                | 317 ms                                                 | 256 ms: 1.24x faster                                                   |
| deepcopy_reduce         | 2.37 us                                                | 1.92 us: 1.24x faster                                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 544 ms: 1.23x faster                                                   |
| docutils                | 1.78 sec                                               | 1.45 sec: 1.23x faster                                                 |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.82 ms: 1.23x faster                                                  |
| bench_thread_pool       | 546 us                                                 | 450 us: 1.21x faster                                                   |
| sqlglot_optimize        | 38.0 ms                                                | 31.4 ms: 1.21x faster                                                  |
| python_startup_no_site  | 8.88 ms                                                | 7.39 ms: 1.20x faster                                                  |
| sympy_integrate         | 13.3 ms                                                | 11.1 ms: 1.19x faster                                                  |
| scimark_fft             | 230 ms                                                 | 193 ms: 1.19x faster                                                   |
| async_generators        | 234 ms                                                 | 199 ms: 1.17x faster                                                   |
| sympy_str               | 169 ms                                                 | 145 ms: 1.17x faster                                                   |
| sympy_sum               | 93.6 ms                                                | 81.4 ms: 1.15x faster                                                  |
| sympy_expand            | 275 ms                                                 | 240 ms: 1.15x faster                                                   |
| unpack_sequence         | 37.4 ns                                                | 32.7 ns: 1.14x faster                                                  |
| nqueens                 | 68.2 ms                                                | 59.7 ms: 1.14x faster                                                  |
| sqlglot_normalize       | 196 ms                                                 | 172 ms: 1.14x faster                                                   |
| xml_etree_parse         | 106 ms                                                 | 93.7 ms: 1.14x faster                                                  |
| xml_etree_generate      | 54.2 ms                                                | 49.3 ms: 1.10x faster                                                  |
| mdp                     | 1.66 sec                                               | 1.51 sec: 1.10x faster                                                 |
| regex_v8                | 17.6 ms                                                | 16.1 ms: 1.09x faster                                                  |
| 2to3                    | 201 ms                                                 | 185 ms: 1.09x faster                                                   |
| sqlite_synth            | 1.47 us                                                | 1.36 us: 1.09x faster                                                  |
| json                    | 3.08 ms                                                | 2.84 ms: 1.08x faster                                                  |
| telco                   | 3.63 ms                                                | 3.39 ms: 1.07x faster                                                  |
| coroutines              | 20.2 ms                                                | 18.8 ms: 1.07x faster                                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 67.7 ms: 1.07x faster                                                  |
| meteor_contest          | 78.1 ms                                                | 73.8 ms: 1.06x faster                                                  |
| regex_dna               | 162 ms                                                 | 153 ms: 1.06x faster                                                   |
| json_loads              | 16.9 us                                                | 16.2 us: 1.04x faster                                                  |
| pidigits                | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| pickle_dict             | 17.9 us                                                | 17.9 us: 1.00x slower                                                  |
| gc_traversal            | 2.39 ms                                                | 2.41 ms: 1.01x slower                                                  |
| pickle_list             | 2.80 us                                                | 2.83 us: 1.01x slower                                                  |
| pickle                  | 7.35 us                                                | 7.56 us: 1.03x slower                                                  |
| unpickle_list           | 2.69 us                                                | 2.77 us: 1.03x slower                                                  |
| generators              | 32.7 ms                                                | 34.6 ms: 1.06x slower                                                  |
| regex_effbot            | 2.46 ms                                                | 2.60 ms: 1.06x slower                                                  |
| bench_mp_pool           | 39.7 ms                                                | 43.3 ms: 1.09x slower                                                  |
| dask                    | 265 ms                                                 | 318 ms: 1.20x slower                                                   |
| coverage                | 42.0 ms                                                | 56.9 ms: 1.35x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, comprehensions, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230126-3.12.0a4+-9f2c479/bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479.json: mypy
