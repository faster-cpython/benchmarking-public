
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 06249ec
- commit date: 2023-04-01
- overall geometric mean: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 168 ms: 1.19x faster                                   |
| chameleon      | 5.79 ms                                                | 4.50 ms: 1.29x faster                                  |
| docutils       | 1.78 sec                                               | 1.49 sec: 1.19x faster                                 |
| html5lib       | 44.2 ms                                                | 36.8 ms: 1.20x faster                                  |
| tornado_http   | 91.5 ms                                                | 69.7 ms: 1.31x faster                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 60.4 ms: 1.55x faster                                  |
| float          | 72.4 ms                                                | 53.1 ms: 1.36x faster                                  |
| pidigits       | 282 ms                                                 | 280 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 76.8 ms: 1.26x faster                                  |
| regex_v8       | 17.6 ms                                                | 16.1 ms: 1.09x faster                                  |
| regex_dna      | 162 ms                                                 | 152 ms: 1.06x faster                                   |
| regex_effbot   | 2.46 ms                                                | 2.70 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 193 us: 1.46x faster                                   |
| unpickle_pure_python | 203 us                                                 | 148 us: 1.37x faster                                   |
| json_dumps           | 8.40 ms                                                | 6.23 ms: 1.35x faster                                  |
| xml_etree_process    | 44.8 ms                                                | 36.8 ms: 1.22x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 99.1 ms: 1.07x faster                                  |
| xml_etree_generate   | 54.2 ms                                                | 51.3 ms: 1.06x faster                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.03x faster                                  |
| unpickle             | 9.89 us                                                | 9.67 us: 1.02x faster                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 71.3 ms: 1.01x faster                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                  |
| pickle               | 7.35 us                                                | 7.47 us: 1.02x slower                                  |
| pickle_list          | 2.80 us                                                | 2.91 us: 1.04x slower                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.4 ms: 1.04x slower                                  |
| python_startup_no_site | 8.88 ms                                                | 10.2 ms: 1.15x slower                                  |
| Geometric mean         | (ref)                                                  | 1.09x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.40 ms: 1.42x faster                                  |
| genshi_xml      | 37.2 ms                                                | 29.4 ms: 1.27x faster                                  |
| django_template | 27.3 ms                                                | 21.8 ms: 1.25x faster                                  |
| genshi_text     | 18.4 ms                                                | 14.8 ms: 1.24x faster                                  |
| Geometric mean  | (ref)                                                  | 1.29x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.61 ms: 1.97x faster                                  |
| logging_silent          | 119 ns                                                 | 66.8 ns: 1.79x faster                                  |
| richards                | 51.4 ms                                                | 31.4 ms: 1.64x faster                                  |
| nbody                   | 93.3 ms                                                | 60.4 ms: 1.55x faster                                  |
| scimark_lu              | 109 ms                                                 | 71.4 ms: 1.53x faster                                  |
| asyncio_tcp             | 670 ms                                                 | 439 ms: 1.53x faster                                   |
| async_tree_memoization  | 490 ms                                                 | 330 ms: 1.48x faster                                   |
| pickle_pure_python      | 283 us                                                 | 193 us: 1.46x faster                                   |
| raytrace                | 325 ms                                                 | 222 ms: 1.46x faster                                   |
| scimark_sor             | 126 ms                                                 | 88.3 ms: 1.43x faster                                  |
| go                      | 165 ms                                                 | 116 ms: 1.43x faster                                   |
| hexiom                  | 6.32 ms                                                | 4.43 ms: 1.42x faster                                  |
| crypto_pyaes            | 78.1 ms                                                | 54.9 ms: 1.42x faster                                  |
| mako                    | 10.5 ms                                                | 7.40 ms: 1.42x faster                                  |
| chaos                   | 66.7 ms                                                | 47.5 ms: 1.41x faster                                  |
| async_tree_none         | 400 ms                                                 | 289 ms: 1.39x faster                                   |
| async_tree_io           | 1.02 sec                                               | 739 ms: 1.38x faster                                   |
| unpickle_pure_python    | 203 us                                                 | 148 us: 1.37x faster                                   |
| scimark_monte_carlo     | 72.5 ms                                                | 53.0 ms: 1.37x faster                                  |
| float                   | 72.4 ms                                                | 53.1 ms: 1.36x faster                                  |
| json_dumps              | 8.40 ms                                                | 6.23 ms: 1.35x faster                                  |
| pycparser               | 916 ms                                                 | 680 ms: 1.35x faster                                   |
| deepcopy_memo           | 34.4 us                                                | 26.0 us: 1.33x faster                                  |
| pyflate                 | 453 ms                                                 | 343 ms: 1.32x faster                                   |
| tornado_http            | 91.5 ms                                                | 69.7 ms: 1.31x faster                                  |
| spectral_norm           | 95.8 ms                                                | 73.1 ms: 1.31x faster                                  |
| chameleon               | 5.79 ms                                                | 4.50 ms: 1.29x faster                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.07 ms: 1.27x faster                                  |
| pprint_safe_repr        | 606 ms                                                 | 477 ms: 1.27x faster                                   |
| deepcopy                | 281 us                                                 | 222 us: 1.27x faster                                   |
| pprint_pformat          | 1.23 sec                                               | 973 ms: 1.27x faster                                   |
| genshi_xml              | 37.2 ms                                                | 29.4 ms: 1.27x faster                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.25 ms: 1.26x faster                                  |
| logging_simple          | 4.63 us                                                | 3.68 us: 1.26x faster                                  |
| regex_compile           | 96.4 ms                                                | 76.8 ms: 1.26x faster                                  |
| create_gc_cycles        | 880 us                                                 | 701 us: 1.25x faster                                   |
| django_template         | 27.3 ms                                                | 21.8 ms: 1.25x faster                                  |
| logging_format          | 4.97 us                                                | 3.97 us: 1.25x faster                                  |
| thrift                  | 580 us                                                 | 464 us: 1.25x faster                                   |
| genshi_text             | 18.4 ms                                                | 14.8 ms: 1.24x faster                                  |
| dulwich_log             | 37.1 ms                                                | 30.0 ms: 1.24x faster                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 545 ms: 1.23x faster                                   |
| scimark_fft             | 230 ms                                                 | 188 ms: 1.22x faster                                   |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.83 ms: 1.22x faster                                  |
| deepcopy_reduce         | 2.37 us                                                | 1.95 us: 1.22x faster                                  |
| xml_etree_process       | 44.8 ms                                                | 36.8 ms: 1.22x faster                                  |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.34 ms: 1.21x faster                                  |
| html5lib                | 44.2 ms                                                | 36.8 ms: 1.20x faster                                  |
| 2to3                    | 201 ms                                                 | 168 ms: 1.19x faster                                   |
| docutils                | 1.78 sec                                               | 1.49 sec: 1.19x faster                                 |
| generators              | 32.7 ms                                                | 27.6 ms: 1.19x faster                                  |
| sqlglot_optimize        | 38.0 ms                                                | 32.3 ms: 1.17x faster                                  |
| fannkuch                | 317 ms                                                 | 271 ms: 1.17x faster                                   |
| sqlalchemy_declarative  | 74.9 ms                                                | 64.4 ms: 1.16x faster                                  |
| mypy2                   | 307 ms                                                 | 264 ms: 1.16x faster                                   |
| bench_thread_pool       | 546 us                                                 | 472 us: 1.16x faster                                   |
| unpack_sequence         | 37.4 ns                                                | 32.9 ns: 1.14x faster                                  |
| sympy_integrate         | 13.3 ms                                                | 11.8 ms: 1.13x faster                                  |
| sqlglot_normalize       | 196 ms                                                 | 176 ms: 1.12x faster                                   |
| sympy_expand            | 275 ms                                                 | 250 ms: 1.10x faster                                   |
| json                    | 3.08 ms                                                | 2.80 ms: 1.10x faster                                  |
| regex_v8                | 17.6 ms                                                | 16.1 ms: 1.09x faster                                  |
| sympy_str               | 169 ms                                                 | 156 ms: 1.09x faster                                   |
| mdp                     | 1.66 sec                                               | 1.54 sec: 1.08x faster                                 |
| sqlite_synth            | 1.47 us                                                | 1.36 us: 1.08x faster                                  |
| nqueens                 | 68.2 ms                                                | 63.3 ms: 1.08x faster                                  |
| xml_etree_parse         | 106 ms                                                 | 99.1 ms: 1.07x faster                                  |
| meteor_contest          | 78.1 ms                                                | 72.7 ms: 1.07x faster                                  |
| coroutines              | 20.2 ms                                                | 18.9 ms: 1.07x faster                                  |
| regex_dna               | 162 ms                                                 | 152 ms: 1.06x faster                                   |
| xml_etree_generate      | 54.2 ms                                                | 51.3 ms: 1.06x faster                                  |
| sympy_sum               | 93.6 ms                                                | 88.8 ms: 1.05x faster                                  |
| pathlib                 | 28.8 ms                                                | 27.6 ms: 1.04x faster                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.03x faster                                  |
| telco                   | 3.63 ms                                                | 3.54 ms: 1.02x faster                                  |
| unpickle                | 9.89 us                                                | 9.67 us: 1.02x faster                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 71.3 ms: 1.01x faster                                  |
| pidigits                | 282 ms                                                 | 280 ms: 1.01x faster                                   |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                  |
| comprehensions          | 17.6 us                                                | 17.8 us: 1.01x slower                                  |
| gc_traversal            | 2.39 ms                                                | 2.43 ms: 1.01x slower                                  |
| pickle                  | 7.35 us                                                | 7.47 us: 1.02x slower                                  |
| pickle_list             | 2.80 us                                                | 2.91 us: 1.04x slower                                  |
| python_startup          | 11.9 ms                                                | 12.4 ms: 1.04x slower                                  |
| regex_effbot            | 2.46 ms                                                | 2.70 ms: 1.10x slower                                  |
| async_generators        | 234 ms                                                 | 265 ms: 1.13x slower                                   |
| python_startup_no_site  | 8.88 ms                                                | 10.2 ms: 1.15x slower                                  |
| bench_mp_pool           | 39.7 ms                                                | 46.4 ms: 1.17x slower                                  |
| dask                    | 265 ms                                                 | 327 ms: 1.23x slower                                   |
| coverage                | 42.0 ms                                                | 60.5 ms: 1.44x slower                                  |
| Geometric mean          | (ref)                                                  | 1.19x faster                                           |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint
