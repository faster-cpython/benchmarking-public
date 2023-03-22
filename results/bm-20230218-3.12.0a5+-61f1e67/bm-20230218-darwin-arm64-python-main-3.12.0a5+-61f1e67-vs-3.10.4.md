
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 61f1e67
- commit date: 2023-02-18
- overall geometric mean: 1.22x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 161 ms: 1.25x faster                                   |
| chameleon      | 5.79 ms                                                | 4.45 ms: 1.30x faster                                  |
| docutils       | 1.78 sec                                               | 1.48 sec: 1.21x faster                                 |
| html5lib       | 44.2 ms                                                | 35.5 ms: 1.25x faster                                  |
| tornado_http   | 91.5 ms                                                | 70.2 ms: 1.30x faster                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 64.1 ms: 1.46x faster                                  |
| float          | 72.4 ms                                                | 52.4 ms: 1.38x faster                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 72.9 ms: 1.32x faster                                  |
| regex_v8       | 17.6 ms                                                | 15.7 ms: 1.12x faster                                  |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                   |
| regex_effbot   | 2.46 ms                                                | 2.60 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 193 us: 1.47x faster                                   |
| unpickle_pure_python | 203 us                                                 | 142 us: 1.43x faster                                   |
| json_dumps           | 8.40 ms                                                | 6.16 ms: 1.36x faster                                  |
| xml_etree_process    | 44.8 ms                                                | 35.9 ms: 1.25x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 96.6 ms: 1.10x faster                                  |
| xml_etree_generate   | 54.2 ms                                                | 50.2 ms: 1.08x faster                                  |
| unpickle_list        | 2.69 us                                                | 2.56 us: 1.05x faster                                  |
| json_loads           | 16.9 us                                                | 16.1 us: 1.05x faster                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 69.8 ms: 1.04x faster                                  |
| unpickle             | 9.89 us                                                | 9.70 us: 1.02x faster                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                  |
| pickle               | 7.35 us                                                | 7.50 us: 1.02x slower                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 11.4 ms: 1.05x faster                                  |
| python_startup_no_site | 8.88 ms                                                | 9.34 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.00x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.35 ms: 1.43x faster                                  |
| genshi_xml      | 37.2 ms                                                | 28.2 ms: 1.32x faster                                  |
| genshi_text     | 18.4 ms                                                | 14.3 ms: 1.29x faster                                  |
| django_template | 27.3 ms                                                | 21.3 ms: 1.28x faster                                  |
| Geometric mean  | (ref)                                                  | 1.33x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.56 ms: 2.01x faster                                  |
| logging_silent          | 119 ns                                                 | 66.0 ns: 1.81x faster                                  |
| richards                | 51.4 ms                                                | 29.9 ms: 1.72x faster                                  |
| go                      | 165 ms                                                 | 108 ms: 1.53x faster                                   |
| async_tree_memoization  | 490 ms                                                 | 325 ms: 1.51x faster                                   |
| scimark_lu              | 109 ms                                                 | 72.7 ms: 1.50x faster                                  |
| hexiom                  | 6.32 ms                                                | 4.30 ms: 1.47x faster                                  |
| asyncio_tcp             | 670 ms                                                 | 456 ms: 1.47x faster                                   |
| scimark_sor             | 126 ms                                                 | 85.9 ms: 1.47x faster                                  |
| pickle_pure_python      | 283 us                                                 | 193 us: 1.47x faster                                   |
| raytrace                | 325 ms                                                 | 223 ms: 1.46x faster                                   |
| crypto_pyaes            | 78.1 ms                                                | 53.5 ms: 1.46x faster                                  |
| nbody                   | 93.3 ms                                                | 64.1 ms: 1.46x faster                                  |
| chaos                   | 66.7 ms                                                | 46.5 ms: 1.44x faster                                  |
| unpickle_pure_python    | 203 us                                                 | 142 us: 1.43x faster                                   |
| mako                    | 10.5 ms                                                | 7.35 ms: 1.43x faster                                  |
| async_tree_none         | 400 ms                                                 | 283 ms: 1.41x faster                                   |
| pyflate                 | 453 ms                                                 | 325 ms: 1.40x faster                                   |
| scimark_monte_carlo     | 72.5 ms                                                | 52.4 ms: 1.38x faster                                  |
| async_tree_io           | 1.02 sec                                               | 736 ms: 1.38x faster                                   |
| pycparser               | 916 ms                                                 | 662 ms: 1.38x faster                                   |
| float                   | 72.4 ms                                                | 52.4 ms: 1.38x faster                                  |
| json_dumps              | 8.40 ms                                                | 6.16 ms: 1.36x faster                                  |
| deepcopy_memo           | 34.4 us                                                | 25.3 us: 1.36x faster                                  |
| regex_compile           | 96.4 ms                                                | 72.9 ms: 1.32x faster                                  |
| genshi_xml              | 37.2 ms                                                | 28.2 ms: 1.32x faster                                  |
| tornado_http            | 91.5 ms                                                | 70.2 ms: 1.30x faster                                  |
| chameleon               | 5.79 ms                                                | 4.45 ms: 1.30x faster                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.05 ms: 1.30x faster                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.22 ms: 1.29x faster                                  |
| genshi_text             | 18.4 ms                                                | 14.3 ms: 1.29x faster                                  |
| pprint_safe_repr        | 606 ms                                                 | 470 ms: 1.29x faster                                   |
| pprint_pformat          | 1.23 sec                                               | 959 ms: 1.28x faster                                   |
| logging_simple          | 4.63 us                                                | 3.61 us: 1.28x faster                                  |
| generators              | 32.7 ms                                                | 25.5 ms: 1.28x faster                                  |
| django_template         | 27.3 ms                                                | 21.3 ms: 1.28x faster                                  |
| deepcopy                | 281 us                                                 | 220 us: 1.28x faster                                   |
| logging_format          | 4.97 us                                                | 3.89 us: 1.28x faster                                  |
| spectral_norm           | 95.8 ms                                                | 75.2 ms: 1.28x faster                                  |
| thrift                  | 580 us                                                 | 458 us: 1.27x faster                                   |
| dulwich_log             | 37.1 ms                                                | 29.5 ms: 1.26x faster                                  |
| create_gc_cycles        | 880 us                                                 | 704 us: 1.25x faster                                   |
| 2to3                    | 201 ms                                                 | 161 ms: 1.25x faster                                   |
| xml_etree_process       | 44.8 ms                                                | 35.9 ms: 1.25x faster                                  |
| html5lib                | 44.2 ms                                                | 35.5 ms: 1.25x faster                                  |
| fannkuch                | 317 ms                                                 | 255 ms: 1.24x faster                                   |
| async_tree_cpu_io_mixed | 669 ms                                                 | 541 ms: 1.24x faster                                   |
| deepcopy_reduce         | 2.37 us                                                | 1.93 us: 1.23x faster                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.81 ms: 1.23x faster                                  |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.24 ms: 1.23x faster                                  |
| docutils                | 1.78 sec                                               | 1.48 sec: 1.21x faster                                 |
| sqlglot_optimize        | 38.0 ms                                                | 31.8 ms: 1.20x faster                                  |
| mypy2                   | 307 ms                                                 | 257 ms: 1.19x faster                                   |
| scimark_fft             | 230 ms                                                 | 193 ms: 1.19x faster                                   |
| sqlalchemy_declarative  | 74.9 ms                                                | 63.4 ms: 1.18x faster                                  |
| bench_thread_pool       | 546 us                                                 | 463 us: 1.18x faster                                   |
| sympy_integrate         | 13.3 ms                                                | 11.3 ms: 1.17x faster                                  |
| sympy_str               | 169 ms                                                 | 147 ms: 1.15x faster                                   |
| unpack_sequence         | 37.4 ns                                                | 32.7 ns: 1.15x faster                                  |
| coroutines              | 20.2 ms                                                | 17.7 ms: 1.14x faster                                  |
| sympy_expand            | 275 ms                                                 | 243 ms: 1.13x faster                                   |
| sqlglot_normalize       | 196 ms                                                 | 173 ms: 1.13x faster                                   |
| sympy_sum               | 93.6 ms                                                | 83.5 ms: 1.12x faster                                  |
| regex_v8                | 17.6 ms                                                | 15.7 ms: 1.12x faster                                  |
| nqueens                 | 68.2 ms                                                | 61.1 ms: 1.12x faster                                  |
| json                    | 3.08 ms                                                | 2.77 ms: 1.11x faster                                  |
| xml_etree_parse         | 106 ms                                                 | 96.6 ms: 1.10x faster                                  |
| sqlite_synth            | 1.47 us                                                | 1.36 us: 1.09x faster                                  |
| mdp                     | 1.66 sec                                               | 1.53 sec: 1.08x faster                                 |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                   |
| xml_etree_generate      | 54.2 ms                                                | 50.2 ms: 1.08x faster                                  |
| pathlib                 | 28.8 ms                                                | 27.4 ms: 1.05x faster                                  |
| unpickle_list           | 2.69 us                                                | 2.56 us: 1.05x faster                                  |
| json_loads              | 16.9 us                                                | 16.1 us: 1.05x faster                                  |
| python_startup          | 11.9 ms                                                | 11.4 ms: 1.05x faster                                  |
| telco                   | 3.63 ms                                                | 3.47 ms: 1.05x faster                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 69.8 ms: 1.04x faster                                  |
| meteor_contest          | 78.1 ms                                                | 75.8 ms: 1.03x faster                                  |
| unpickle                | 9.89 us                                                | 9.70 us: 1.02x faster                                  |
| pidigits                | 282 ms                                                 | 281 ms: 1.01x faster                                   |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                  |
| gc_traversal            | 2.39 ms                                                | 2.42 ms: 1.01x slower                                  |
| pickle                  | 7.35 us                                                | 7.50 us: 1.02x slower                                  |
| python_startup_no_site  | 8.88 ms                                                | 9.34 ms: 1.05x slower                                  |
| regex_effbot            | 2.46 ms                                                | 2.60 ms: 1.06x slower                                  |
| async_generators        | 234 ms                                                 | 263 ms: 1.12x slower                                   |
| bench_mp_pool           | 39.7 ms                                                | 45.0 ms: 1.13x slower                                  |
| dask                    | 265 ms                                                 | 318 ms: 1.20x slower                                   |
| coverage                | 42.0 ms                                                | 61.0 ms: 1.45x slower                                  |
| Geometric mean          | (ref)                                                  | 1.22x faster                                           |

Benchmark hidden because not significant (1): pickle_list
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, comprehensions, flaskblogging, gunicorn, pylint
