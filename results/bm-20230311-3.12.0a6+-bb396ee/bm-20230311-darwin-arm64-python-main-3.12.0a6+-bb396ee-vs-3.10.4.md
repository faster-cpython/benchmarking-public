
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: bb396ee
- commit date: 2023-03-11
- overall geometric mean: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 166 ms: 1.21x faster                                   |
| chameleon      | 5.79 ms                                                | 4.51 ms: 1.28x faster                                  |
| docutils       | 1.78 sec                                               | 1.49 sec: 1.19x faster                                 |
| html5lib       | 44.2 ms                                                | 35.8 ms: 1.24x faster                                  |
| tornado_http   | 91.5 ms                                                | 68.7 ms: 1.33x faster                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 64.1 ms: 1.46x faster                                  |
| float          | 72.4 ms                                                | 53.6 ms: 1.35x faster                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 75.7 ms: 1.27x faster                                  |
| regex_v8       | 17.6 ms                                                | 16.1 ms: 1.09x faster                                  |
| regex_dna      | 162 ms                                                 | 152 ms: 1.07x faster                                   |
| regex_effbot   | 2.46 ms                                                | 2.69 ms: 1.09x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 190 us: 1.49x faster                                   |
| unpickle_pure_python | 203 us                                                 | 145 us: 1.40x faster                                   |
| json_dumps           | 8.40 ms                                                | 6.30 ms: 1.33x faster                                  |
| xml_etree_process    | 44.8 ms                                                | 36.8 ms: 1.22x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 97.2 ms: 1.09x faster                                  |
| xml_etree_generate   | 54.2 ms                                                | 51.0 ms: 1.06x faster                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 70.8 ms: 1.02x faster                                  |
| unpickle             | 9.89 us                                                | 9.76 us: 1.01x faster                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| pickle               | 7.35 us                                                | 7.48 us: 1.02x slower                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                           |

Benchmark hidden because not significant (2): unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 11.1 ms: 1.08x faster                                  |
| python_startup_no_site | 8.88 ms                                                | 8.93 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.47 ms: 1.40x faster                                  |
| genshi_xml      | 37.2 ms                                                | 29.4 ms: 1.27x faster                                  |
| django_template | 27.3 ms                                                | 21.7 ms: 1.26x faster                                  |
| genshi_text     | 18.4 ms                                                | 14.9 ms: 1.24x faster                                  |
| Geometric mean  | (ref)                                                  | 1.29x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.59 ms: 1.99x faster                                  |
| logging_silent          | 119 ns                                                 | 68.9 ns: 1.73x faster                                  |
| richards                | 51.4 ms                                                | 30.7 ms: 1.67x faster                                  |
| asyncio_tcp             | 670 ms                                                 | 414 ms: 1.62x faster                                   |
| go                      | 165 ms                                                 | 111 ms: 1.49x faster                                   |
| pickle_pure_python      | 283 us                                                 | 190 us: 1.49x faster                                   |
| async_tree_memoization  | 490 ms                                                 | 336 ms: 1.46x faster                                   |
| scimark_lu              | 109 ms                                                 | 75.0 ms: 1.46x faster                                  |
| nbody                   | 93.3 ms                                                | 64.1 ms: 1.46x faster                                  |
| crypto_pyaes            | 78.1 ms                                                | 53.7 ms: 1.45x faster                                  |
| scimark_sor             | 126 ms                                                 | 88.4 ms: 1.43x faster                                  |
| raytrace                | 325 ms                                                 | 228 ms: 1.43x faster                                   |
| hexiom                  | 6.32 ms                                                | 4.45 ms: 1.42x faster                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 51.3 ms: 1.41x faster                                  |
| mako                    | 10.5 ms                                                | 7.47 ms: 1.40x faster                                  |
| unpickle_pure_python    | 203 us                                                 | 145 us: 1.40x faster                                   |
| chaos                   | 66.7 ms                                                | 47.9 ms: 1.39x faster                                  |
| async_tree_none         | 400 ms                                                 | 290 ms: 1.38x faster                                   |
| async_tree_io           | 1.02 sec                                               | 745 ms: 1.37x faster                                   |
| pyflate                 | 453 ms                                                 | 332 ms: 1.36x faster                                   |
| float                   | 72.4 ms                                                | 53.6 ms: 1.35x faster                                  |
| pycparser               | 916 ms                                                 | 678 ms: 1.35x faster                                   |
| json_dumps              | 8.40 ms                                                | 6.30 ms: 1.33x faster                                  |
| tornado_http            | 91.5 ms                                                | 68.7 ms: 1.33x faster                                  |
| deepcopy_memo           | 34.4 us                                                | 26.3 us: 1.31x faster                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.06 ms: 1.29x faster                                  |
| chameleon               | 5.79 ms                                                | 4.51 ms: 1.28x faster                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.23 ms: 1.28x faster                                  |
| thrift                  | 580 us                                                 | 453 us: 1.28x faster                                   |
| spectral_norm           | 95.8 ms                                                | 75.0 ms: 1.28x faster                                  |
| regex_compile           | 96.4 ms                                                | 75.7 ms: 1.27x faster                                  |
| logging_simple          | 4.63 us                                                | 3.64 us: 1.27x faster                                  |
| genshi_xml              | 37.2 ms                                                | 29.4 ms: 1.27x faster                                  |
| logging_format          | 4.97 us                                                | 3.94 us: 1.26x faster                                  |
| pprint_pformat          | 1.23 sec                                               | 979 ms: 1.26x faster                                   |
| pprint_safe_repr        | 606 ms                                                 | 481 ms: 1.26x faster                                   |
| django_template         | 27.3 ms                                                | 21.7 ms: 1.26x faster                                  |
| dulwich_log             | 37.1 ms                                                | 29.6 ms: 1.25x faster                                  |
| create_gc_cycles        | 880 us                                                 | 704 us: 1.25x faster                                   |
| deepcopy                | 281 us                                                 | 225 us: 1.25x faster                                   |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.18 ms: 1.24x faster                                  |
| genshi_text             | 18.4 ms                                                | 14.9 ms: 1.24x faster                                  |
| html5lib                | 44.2 ms                                                | 35.8 ms: 1.24x faster                                  |
| fannkuch                | 317 ms                                                 | 257 ms: 1.23x faster                                   |
| async_tree_cpu_io_mixed | 669 ms                                                 | 548 ms: 1.22x faster                                   |
| xml_etree_process       | 44.8 ms                                                | 36.8 ms: 1.22x faster                                  |
| 2to3                    | 201 ms                                                 | 166 ms: 1.21x faster                                   |
| deepcopy_reduce         | 2.37 us                                                | 1.97 us: 1.20x faster                                  |
| docutils                | 1.78 sec                                               | 1.49 sec: 1.19x faster                                 |
| sqlglot_optimize        | 38.0 ms                                                | 32.2 ms: 1.18x faster                                  |
| scimark_fft             | 230 ms                                                 | 196 ms: 1.17x faster                                   |
| mypy2                   | 307 ms                                                 | 262 ms: 1.17x faster                                   |
| sqlalchemy_declarative  | 74.9 ms                                                | 64.3 ms: 1.17x faster                                  |
| generators              | 32.7 ms                                                | 28.2 ms: 1.16x faster                                  |
| bench_thread_pool       | 546 us                                                 | 473 us: 1.16x faster                                   |
| unpack_sequence         | 37.4 ns                                                | 32.8 ns: 1.14x faster                                  |
| sympy_integrate         | 13.3 ms                                                | 11.8 ms: 1.13x faster                                  |
| sqlglot_normalize       | 196 ms                                                 | 175 ms: 1.12x faster                                   |
| coroutines              | 20.2 ms                                                | 18.1 ms: 1.12x faster                                  |
| mdp                     | 1.66 sec                                               | 1.50 sec: 1.11x faster                                 |
| sympy_expand            | 275 ms                                                 | 248 ms: 1.11x faster                                   |
| xml_etree_parse         | 106 ms                                                 | 97.2 ms: 1.09x faster                                  |
| sympy_str               | 169 ms                                                 | 155 ms: 1.09x faster                                   |
| regex_v8                | 17.6 ms                                                | 16.1 ms: 1.09x faster                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.17 ms: 1.09x faster                                  |
| sqlite_synth            | 1.47 us                                                | 1.36 us: 1.09x faster                                  |
| json                    | 3.08 ms                                                | 2.84 ms: 1.08x faster                                  |
| nqueens                 | 68.2 ms                                                | 62.9 ms: 1.08x faster                                  |
| python_startup          | 11.9 ms                                                | 11.1 ms: 1.08x faster                                  |
| telco                   | 3.63 ms                                                | 3.40 ms: 1.07x faster                                  |
| regex_dna               | 162 ms                                                 | 152 ms: 1.07x faster                                   |
| xml_etree_generate      | 54.2 ms                                                | 51.0 ms: 1.06x faster                                  |
| meteor_contest          | 78.1 ms                                                | 73.8 ms: 1.06x faster                                  |
| sympy_sum               | 93.6 ms                                                | 88.7 ms: 1.06x faster                                  |
| pathlib                 | 28.8 ms                                                | 27.5 ms: 1.05x faster                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.04x faster                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 70.8 ms: 1.02x faster                                  |
| unpickle                | 9.89 us                                                | 9.76 us: 1.01x faster                                  |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                   |
| python_startup_no_site  | 8.88 ms                                                | 8.93 ms: 1.01x slower                                  |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| gc_traversal            | 2.39 ms                                                | 2.43 ms: 1.01x slower                                  |
| pickle                  | 7.35 us                                                | 7.48 us: 1.02x slower                                  |
| comprehensions          | 17.6 us                                                | 17.9 us: 1.02x slower                                  |
| regex_effbot            | 2.46 ms                                                | 2.69 ms: 1.09x slower                                  |
| bench_mp_pool           | 39.7 ms                                                | 45.2 ms: 1.14x slower                                  |
| async_generators        | 234 ms                                                 | 267 ms: 1.14x slower                                   |
| dask                    | 265 ms                                                 | 323 ms: 1.22x slower                                   |
| coverage                | 42.0 ms                                                | 59.7 ms: 1.42x slower                                  |
| Geometric mean          | (ref)                                                  | 1.20x faster                                           |

Benchmark hidden because not significant (2): unpickle_list, pickle_list
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint
