
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 666c084
- commit date: 2023-01-28
- overall geometric mean: 1.23x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-darwin-arm64-python-main-3.12.0a4+-666c084 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 185 ms: 1.09x faster                                   |
| chameleon      | 5.79 ms                                                | 4.58 ms: 1.26x faster                                  |
| docutils       | 1.78 sec                                               | 1.45 sec: 1.23x faster                                 |
| html5lib       | 44.2 ms                                                | 35.2 ms: 1.25x faster                                  |
| tornado_http   | 91.5 ms                                                | 70.3 ms: 1.30x faster                                  |
| Geometric mean | (ref)                                                  | 1.22x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-darwin-arm64-python-main-3.12.0a4+-666c084 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 64.2 ms: 1.45x faster                                  |
| float          | 72.4 ms                                                | 51.7 ms: 1.40x faster                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-darwin-arm64-python-main-3.12.0a4+-666c084 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 73.6 ms: 1.31x faster                                  |
| regex_v8       | 17.6 ms                                                | 16.1 ms: 1.09x faster                                  |
| regex_dna      | 162 ms                                                 | 150 ms: 1.08x faster                                   |
| regex_effbot   | 2.46 ms                                                | 2.65 ms: 1.08x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-darwin-arm64-python-main-3.12.0a4+-666c084 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 192 us: 1.47x faster                                   |
| unpickle_pure_python | 203 us                                                 | 148 us: 1.37x faster                                   |
| json_dumps           | 8.40 ms                                                | 6.13 ms: 1.37x faster                                  |
| xml_etree_process    | 44.8 ms                                                | 35.8 ms: 1.25x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 93.9 ms: 1.13x faster                                  |
| xml_etree_generate   | 54.2 ms                                                | 49.4 ms: 1.10x faster                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 67.9 ms: 1.06x faster                                  |
| json_loads           | 16.9 us                                                | 16.4 us: 1.03x faster                                  |
| unpickle_list        | 2.69 us                                                | 2.73 us: 1.02x slower                                  |
| pickle_list          | 2.80 us                                                | 2.86 us: 1.02x slower                                  |
| pickle               | 7.35 us                                                | 7.52 us: 1.02x slower                                  |
| unpickle             | 9.89 us                                                | 10.1 us: 1.03x slower                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                           |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-darwin-arm64-python-main-3.12.0a4+-666c084 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.40 ms: 1.27x faster                                  |
| python_startup_no_site | 8.88 ms                                                | 7.39 ms: 1.20x faster                                  |
| Geometric mean         | (ref)                                                  | 1.23x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-darwin-arm64-python-main-3.12.0a4+-666c084 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.25 ms: 1.45x faster                                  |
| genshi_xml      | 37.2 ms                                                | 29.0 ms: 1.28x faster                                  |
| django_template | 27.3 ms                                                | 21.3 ms: 1.28x faster                                  |
| genshi_text     | 18.4 ms                                                | 14.7 ms: 1.25x faster                                  |
| Geometric mean  | (ref)                                                  | 1.31x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-darwin-arm64-python-main-3.12.0a4+-666c084 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.50 ms: 2.06x faster                                  |
| logging_silent          | 119 ns                                                 | 66.4 ns: 1.80x faster                                  |
| richards                | 51.4 ms                                                | 31.0 ms: 1.66x faster                                  |
| scimark_sor             | 126 ms                                                 | 77.8 ms: 1.62x faster                                  |
| asyncio_tcp             | 670 ms                                                 | 422 ms: 1.59x faster                                   |
| raytrace                | 325 ms                                                 | 208 ms: 1.56x faster                                   |
| scimark_lu              | 109 ms                                                 | 70.7 ms: 1.55x faster                                  |
| async_tree_memoization  | 490 ms                                                 | 323 ms: 1.52x faster                                   |
| crypto_pyaes            | 78.1 ms                                                | 51.9 ms: 1.50x faster                                  |
| go                      | 165 ms                                                 | 111 ms: 1.49x faster                                   |
| scimark_monte_carlo     | 72.5 ms                                                | 48.9 ms: 1.48x faster                                  |
| pickle_pure_python      | 283 us                                                 | 192 us: 1.47x faster                                   |
| nbody                   | 93.3 ms                                                | 64.2 ms: 1.45x faster                                  |
| mako                    | 10.5 ms                                                | 7.25 ms: 1.45x faster                                  |
| float                   | 72.4 ms                                                | 51.7 ms: 1.40x faster                                  |
| pyflate                 | 453 ms                                                 | 324 ms: 1.40x faster                                   |
| pathlib                 | 28.8 ms                                                | 20.6 ms: 1.40x faster                                  |
| chaos                   | 66.7 ms                                                | 47.7 ms: 1.40x faster                                  |
| async_tree_none         | 400 ms                                                 | 288 ms: 1.39x faster                                   |
| async_tree_io           | 1.02 sec                                               | 740 ms: 1.38x faster                                   |
| unpickle_pure_python    | 203 us                                                 | 148 us: 1.37x faster                                   |
| json_dumps              | 8.40 ms                                                | 6.13 ms: 1.37x faster                                  |
| pycparser               | 916 ms                                                 | 680 ms: 1.35x faster                                   |
| sqlglot_parse           | 1.37 ms                                                | 1.02 ms: 1.35x faster                                  |
| hexiom                  | 6.32 ms                                                | 4.70 ms: 1.34x faster                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.18 ms: 1.33x faster                                  |
| spectral_norm           | 95.8 ms                                                | 72.3 ms: 1.33x faster                                  |
| deepcopy_memo           | 34.4 us                                                | 26.0 us: 1.32x faster                                  |
| logging_simple          | 4.63 us                                                | 3.51 us: 1.32x faster                                  |
| logging_format          | 4.97 us                                                | 3.79 us: 1.31x faster                                  |
| regex_compile           | 96.4 ms                                                | 73.6 ms: 1.31x faster                                  |
| tornado_http            | 91.5 ms                                                | 70.3 ms: 1.30x faster                                  |
| dulwich_log             | 37.1 ms                                                | 28.5 ms: 1.30x faster                                  |
| pprint_pformat          | 1.23 sec                                               | 950 ms: 1.30x faster                                   |
| thrift                  | 580 us                                                 | 449 us: 1.29x faster                                   |
| pprint_safe_repr        | 606 ms                                                 | 468 ms: 1.29x faster                                   |
| deepcopy                | 281 us                                                 | 219 us: 1.29x faster                                   |
| genshi_xml              | 37.2 ms                                                | 29.0 ms: 1.28x faster                                  |
| django_template         | 27.3 ms                                                | 21.3 ms: 1.28x faster                                  |
| create_gc_cycles        | 880 us                                                 | 688 us: 1.28x faster                                   |
| python_startup          | 11.9 ms                                                | 9.40 ms: 1.27x faster                                  |
| chameleon               | 5.79 ms                                                | 4.58 ms: 1.26x faster                                  |
| deepcopy_reduce         | 2.37 us                                                | 1.88 us: 1.26x faster                                  |
| html5lib                | 44.2 ms                                                | 35.2 ms: 1.25x faster                                  |
| xml_etree_process       | 44.8 ms                                                | 35.8 ms: 1.25x faster                                  |
| genshi_text             | 18.4 ms                                                | 14.7 ms: 1.25x faster                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.79 ms: 1.24x faster                                  |
| fannkuch                | 317 ms                                                 | 258 ms: 1.23x faster                                   |
| async_tree_cpu_io_mixed | 669 ms                                                 | 544 ms: 1.23x faster                                   |
| docutils                | 1.78 sec                                               | 1.45 sec: 1.23x faster                                 |
| bench_thread_pool       | 546 us                                                 | 450 us: 1.21x faster                                   |
| sqlglot_optimize        | 38.0 ms                                                | 31.4 ms: 1.21x faster                                  |
| python_startup_no_site  | 8.88 ms                                                | 7.39 ms: 1.20x faster                                  |
| scimark_fft             | 230 ms                                                 | 192 ms: 1.20x faster                                   |
| sympy_integrate         | 13.3 ms                                                | 11.1 ms: 1.19x faster                                  |
| async_generators        | 234 ms                                                 | 200 ms: 1.17x faster                                   |
| sympy_str               | 169 ms                                                 | 145 ms: 1.17x faster                                   |
| sympy_expand            | 275 ms                                                 | 240 ms: 1.15x faster                                   |
| sympy_sum               | 93.6 ms                                                | 81.9 ms: 1.14x faster                                  |
| unpack_sequence         | 37.4 ns                                                | 32.8 ns: 1.14x faster                                  |
| sqlglot_normalize       | 196 ms                                                 | 172 ms: 1.14x faster                                   |
| nqueens                 | 68.2 ms                                                | 59.9 ms: 1.14x faster                                  |
| xml_etree_parse         | 106 ms                                                 | 93.9 ms: 1.13x faster                                  |
| mdp                     | 1.66 sec                                               | 1.51 sec: 1.10x faster                                 |
| xml_etree_generate      | 54.2 ms                                                | 49.4 ms: 1.10x faster                                  |
| regex_v8                | 17.6 ms                                                | 16.1 ms: 1.09x faster                                  |
| 2to3                    | 201 ms                                                 | 185 ms: 1.09x faster                                   |
| sqlite_synth            | 1.47 us                                                | 1.36 us: 1.09x faster                                  |
| regex_dna               | 162 ms                                                 | 150 ms: 1.08x faster                                   |
| json                    | 3.08 ms                                                | 2.86 ms: 1.08x faster                                  |
| coroutines              | 20.2 ms                                                | 18.8 ms: 1.07x faster                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 67.9 ms: 1.06x faster                                  |
| telco                   | 3.63 ms                                                | 3.43 ms: 1.06x faster                                  |
| meteor_contest          | 78.1 ms                                                | 73.8 ms: 1.06x faster                                  |
| json_loads              | 16.9 us                                                | 16.4 us: 1.03x faster                                  |
| pidigits                | 282 ms                                                 | 283 ms: 1.00x slower                                   |
| gc_traversal            | 2.39 ms                                                | 2.41 ms: 1.01x slower                                  |
| unpickle_list           | 2.69 us                                                | 2.73 us: 1.02x slower                                  |
| pickle_list             | 2.80 us                                                | 2.86 us: 1.02x slower                                  |
| pickle                  | 7.35 us                                                | 7.52 us: 1.02x slower                                  |
| unpickle                | 9.89 us                                                | 10.1 us: 1.03x slower                                  |
| generators              | 32.7 ms                                                | 34.7 ms: 1.06x slower                                  |
| bench_mp_pool           | 39.7 ms                                                | 42.6 ms: 1.07x slower                                  |
| regex_effbot            | 2.46 ms                                                | 2.65 ms: 1.08x slower                                  |
| dask                    | 265 ms                                                 | 319 ms: 1.20x slower                                   |
| coverage                | 42.0 ms                                                | 57.1 ms: 1.36x slower                                  |
| Geometric mean          | (ref)                                                  | 1.23x faster                                           |

Benchmark hidden because not significant (1): pickle_dict
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, comprehensions, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230128-3.12.0a4+-666c084/bm-20230128-darwin-arm64-python-main-3.12.0a4+-666c084.json: mypy
