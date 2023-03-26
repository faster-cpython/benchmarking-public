
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 30a306c
- commit date: 2023-03-25
- overall geometric mean: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 168 ms: 1.19x faster                                   |
| chameleon      | 5.79 ms                                                | 4.51 ms: 1.29x faster                                  |
| docutils       | 1.78 sec                                               | 1.51 sec: 1.18x faster                                 |
| html5lib       | 44.2 ms                                                | 36.7 ms: 1.20x faster                                  |
| tornado_http   | 91.5 ms                                                | 69.1 ms: 1.33x faster                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 60.6 ms: 1.54x faster                                  |
| float          | 72.4 ms                                                | 53.1 ms: 1.36x faster                                  |
| pidigits       | 282 ms                                                 | 280 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 77.0 ms: 1.25x faster                                  |
| regex_v8       | 17.6 ms                                                | 16.1 ms: 1.09x faster                                  |
| regex_dna      | 162 ms                                                 | 152 ms: 1.06x faster                                   |
| regex_effbot   | 2.46 ms                                                | 2.71 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 194 us: 1.46x faster                                   |
| unpickle_pure_python | 203 us                                                 | 151 us: 1.35x faster                                   |
| json_dumps           | 8.40 ms                                                | 6.24 ms: 1.35x faster                                  |
| xml_etree_process    | 44.8 ms                                                | 37.0 ms: 1.21x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 97.8 ms: 1.09x faster                                  |
| xml_etree_generate   | 54.2 ms                                                | 52.0 ms: 1.04x faster                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 70.7 ms: 1.02x faster                                  |
| unpickle             | 9.89 us                                                | 9.71 us: 1.02x faster                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| pickle               | 7.35 us                                                | 7.45 us: 1.01x slower                                  |
| pickle_list          | 2.80 us                                                | 2.87 us: 1.02x slower                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.3 ms: 1.03x slower                                  |
| python_startup_no_site | 8.88 ms                                                | 10.3 ms: 1.16x slower                                  |
| Geometric mean         | (ref)                                                  | 1.09x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.40 ms: 1.42x faster                                  |
| genshi_xml      | 37.2 ms                                                | 29.4 ms: 1.26x faster                                  |
| django_template | 27.3 ms                                                | 21.9 ms: 1.25x faster                                  |
| genshi_text     | 18.4 ms                                                | 14.9 ms: 1.23x faster                                  |
| Geometric mean  | (ref)                                                  | 1.29x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.62 ms: 1.96x faster                                  |
| logging_silent          | 119 ns                                                 | 66.6 ns: 1.79x faster                                  |
| richards                | 51.4 ms                                                | 31.5 ms: 1.63x faster                                  |
| nbody                   | 93.3 ms                                                | 60.6 ms: 1.54x faster                                  |
| scimark_lu              | 109 ms                                                 | 71.4 ms: 1.53x faster                                  |
| async_tree_memoization  | 490 ms                                                 | 326 ms: 1.51x faster                                   |
| raytrace                | 325 ms                                                 | 222 ms: 1.46x faster                                   |
| pickle_pure_python      | 283 us                                                 | 194 us: 1.46x faster                                   |
| asyncio_tcp             | 670 ms                                                 | 462 ms: 1.45x faster                                   |
| scimark_sor             | 126 ms                                                 | 88.0 ms: 1.43x faster                                  |
| go                      | 165 ms                                                 | 116 ms: 1.43x faster                                   |
| hexiom                  | 6.32 ms                                                | 4.42 ms: 1.43x faster                                  |
| crypto_pyaes            | 78.1 ms                                                | 54.8 ms: 1.43x faster                                  |
| mako                    | 10.5 ms                                                | 7.40 ms: 1.42x faster                                  |
| chaos                   | 66.7 ms                                                | 47.2 ms: 1.41x faster                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 52.1 ms: 1.39x faster                                  |
| async_tree_none         | 400 ms                                                 | 290 ms: 1.38x faster                                   |
| async_tree_io           | 1.02 sec                                               | 740 ms: 1.38x faster                                   |
| float                   | 72.4 ms                                                | 53.1 ms: 1.36x faster                                  |
| unpickle_pure_python    | 203 us                                                 | 151 us: 1.35x faster                                   |
| pycparser               | 916 ms                                                 | 680 ms: 1.35x faster                                   |
| json_dumps              | 8.40 ms                                                | 6.24 ms: 1.35x faster                                  |
| tornado_http            | 91.5 ms                                                | 69.1 ms: 1.33x faster                                  |
| deepcopy_memo           | 34.4 us                                                | 26.0 us: 1.32x faster                                  |
| pyflate                 | 453 ms                                                 | 343 ms: 1.32x faster                                   |
| spectral_norm           | 95.8 ms                                                | 73.1 ms: 1.31x faster                                  |
| chameleon               | 5.79 ms                                                | 4.51 ms: 1.29x faster                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.07 ms: 1.28x faster                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.25 ms: 1.26x faster                                  |
| thrift                  | 580 us                                                 | 460 us: 1.26x faster                                   |
| genshi_xml              | 37.2 ms                                                | 29.4 ms: 1.26x faster                                  |
| pprint_safe_repr        | 606 ms                                                 | 480 ms: 1.26x faster                                   |
| pprint_pformat          | 1.23 sec                                               | 980 ms: 1.26x faster                                   |
| logging_simple          | 4.63 us                                                | 3.69 us: 1.25x faster                                  |
| deepcopy                | 281 us                                                 | 224 us: 1.25x faster                                   |
| regex_compile           | 96.4 ms                                                | 77.0 ms: 1.25x faster                                  |
| django_template         | 27.3 ms                                                | 21.9 ms: 1.25x faster                                  |
| logging_format          | 4.97 us                                                | 3.99 us: 1.24x faster                                  |
| create_gc_cycles        | 880 us                                                 | 710 us: 1.24x faster                                   |
| genshi_text             | 18.4 ms                                                | 14.9 ms: 1.23x faster                                  |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.23 ms: 1.23x faster                                  |
| dulwich_log             | 37.1 ms                                                | 30.2 ms: 1.23x faster                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 546 ms: 1.22x faster                                   |
| scimark_fft             | 230 ms                                                 | 189 ms: 1.22x faster                                   |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.84 ms: 1.22x faster                                  |
| xml_etree_process       | 44.8 ms                                                | 37.0 ms: 1.21x faster                                  |
| deepcopy_reduce         | 2.37 us                                                | 1.97 us: 1.21x faster                                  |
| generators              | 32.7 ms                                                | 27.1 ms: 1.21x faster                                  |
| html5lib                | 44.2 ms                                                | 36.7 ms: 1.20x faster                                  |
| 2to3                    | 201 ms                                                 | 168 ms: 1.19x faster                                   |
| docutils                | 1.78 sec                                               | 1.51 sec: 1.18x faster                                 |
| sqlglot_optimize        | 38.0 ms                                                | 32.4 ms: 1.17x faster                                  |
| fannkuch                | 317 ms                                                 | 271 ms: 1.17x faster                                   |
| mypy2                   | 307 ms                                                 | 264 ms: 1.16x faster                                   |
| sqlalchemy_declarative  | 74.9 ms                                                | 64.6 ms: 1.16x faster                                  |
| bench_thread_pool       | 546 us                                                 | 475 us: 1.15x faster                                   |
| sympy_integrate         | 13.3 ms                                                | 11.8 ms: 1.13x faster                                  |
| unpack_sequence         | 37.4 ns                                                | 33.3 ns: 1.12x faster                                  |
| sqlglot_normalize       | 196 ms                                                 | 177 ms: 1.11x faster                                   |
| sympy_expand            | 275 ms                                                 | 250 ms: 1.10x faster                                   |
| json                    | 3.08 ms                                                | 2.81 ms: 1.10x faster                                  |
| regex_v8                | 17.6 ms                                                | 16.1 ms: 1.09x faster                                  |
| xml_etree_parse         | 106 ms                                                 | 97.8 ms: 1.09x faster                                  |
| sqlite_synth            | 1.47 us                                                | 1.36 us: 1.09x faster                                  |
| sympy_str               | 169 ms                                                 | 156 ms: 1.08x faster                                   |
| mdp                     | 1.66 sec                                               | 1.54 sec: 1.08x faster                                 |
| coroutines              | 20.2 ms                                                | 18.8 ms: 1.07x faster                                  |
| nqueens                 | 68.2 ms                                                | 63.7 ms: 1.07x faster                                  |
| regex_dna               | 162 ms                                                 | 152 ms: 1.06x faster                                   |
| meteor_contest          | 78.1 ms                                                | 73.8 ms: 1.06x faster                                  |
| sympy_sum               | 93.6 ms                                                | 88.6 ms: 1.06x faster                                  |
| telco                   | 3.63 ms                                                | 3.46 ms: 1.05x faster                                  |
| xml_etree_generate      | 54.2 ms                                                | 52.0 ms: 1.04x faster                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.04x faster                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 70.7 ms: 1.02x faster                                  |
| pathlib                 | 28.8 ms                                                | 28.2 ms: 1.02x faster                                  |
| unpickle                | 9.89 us                                                | 9.71 us: 1.02x faster                                  |
| pidigits                | 282 ms                                                 | 280 ms: 1.01x faster                                   |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| pickle                  | 7.35 us                                                | 7.45 us: 1.01x slower                                  |
| comprehensions          | 17.6 us                                                | 17.8 us: 1.01x slower                                  |
| gc_traversal            | 2.39 ms                                                | 2.43 ms: 1.01x slower                                  |
| pickle_list             | 2.80 us                                                | 2.87 us: 1.02x slower                                  |
| python_startup          | 11.9 ms                                                | 12.3 ms: 1.03x slower                                  |
| regex_effbot            | 2.46 ms                                                | 2.71 ms: 1.10x slower                                  |
| async_generators        | 234 ms                                                 | 267 ms: 1.14x slower                                   |
| python_startup_no_site  | 8.88 ms                                                | 10.3 ms: 1.16x slower                                  |
| bench_mp_pool           | 39.7 ms                                                | 46.2 ms: 1.16x slower                                  |
| dask                    | 265 ms                                                 | 327 ms: 1.23x slower                                   |
| coverage                | 42.0 ms                                                | 60.8 ms: 1.45x slower                                  |
| Geometric mean          | (ref)                                                  | 1.19x faster                                           |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint
