
# Results vs. 3.10.4

- fork: gvanrossum
- ref: e69c1f3e7a01d253e05b
- machine: darwin-arm64
- commit hash: e69c1f3
- commit date: 2023-01-26
- overall geometric mean: 1.23x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 222 ms                                                 | 181 ms: 1.23x faster                                                       |
| chameleon      | 5.86 ms                                                | 4.58 ms: 1.28x faster                                                      |
| docutils       | 1.76 sec                                               | 1.45 sec: 1.22x faster                                                     |
| html5lib       | 44.0 ms                                                | 34.9 ms: 1.26x faster                                                      |
| tornado_http   | 90.1 ms                                                | 70.2 ms: 1.28x faster                                                      |
| Geometric mean | (ref)                                                  | 1.25x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 72.1 ms                                                | 52.4 ms: 1.37x faster                                                      |
| nbody          | 94.6 ms                                                | 64.4 ms: 1.47x faster                                                      |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.27x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 96.2 ms                                                | 73.6 ms: 1.31x faster                                                      |
| regex_dna      | 164 ms                                                 | 150 ms: 1.10x faster                                                       |
| regex_effbot   | 2.45 ms                                                | 2.61 ms: 1.06x slower                                                      |
| regex_v8       | 17.7 ms                                                | 16.1 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                  | 1.11x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 8.34 ms                                                | 6.15 ms: 1.36x faster                                                      |
| json_loads           | 17.0 us                                                | 16.3 us: 1.05x faster                                                      |
| pickle               | 7.50 us                                                | 7.55 us: 1.01x slower                                                      |
| pickle_list          | 2.83 us                                                | 2.84 us: 1.01x slower                                                      |
| pickle_pure_python   | 284 us                                                 | 194 us: 1.46x faster                                                       |
| unpickle             | 10.0 us                                                | 9.87 us: 1.02x faster                                                      |
| unpickle_list        | 2.66 us                                                | 2.71 us: 1.02x slower                                                      |
| unpickle_pure_python | 204 us                                                 | 145 us: 1.40x faster                                                       |
| xml_etree_parse      | 100 ms                                                 | 94.8 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 69.0 ms                                                | 68.3 ms: 1.01x faster                                                      |
| xml_etree_generate   | 54.5 ms                                                | 49.3 ms: 1.11x faster                                                      |
| xml_etree_process    | 45.1 ms                                                | 35.4 ms: 1.27x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                               |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 9.59 ms                                                | 9.40 ms: 1.02x faster                                                      |
| python_startup_no_site | 7.00 ms                                                | 7.38 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 27.2 ms                                                | 21.1 ms: 1.29x faster                                                      |
| genshi_text     | 18.2 ms                                                | 14.8 ms: 1.23x faster                                                      |
| genshi_xml      | 37.7 ms                                                | 28.9 ms: 1.30x faster                                                      |
| mako            | 10.6 ms                                                | 7.29 ms: 1.45x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3                    | 222 ms                                                 | 181 ms: 1.23x faster                                                       |
| async_generators        | 231 ms                                                 | 200 ms: 1.15x faster                                                       |
| async_tree_none         | 396 ms                                                 | 288 ms: 1.37x faster                                                       |
| async_tree_cpu_io_mixed | 665 ms                                                 | 544 ms: 1.22x faster                                                       |
| async_tree_io           | 1.01 sec                                               | 743 ms: 1.36x faster                                                       |
| async_tree_memoization  | 485 ms                                                 | 332 ms: 1.46x faster                                                       |
| chameleon               | 5.86 ms                                                | 4.58 ms: 1.28x faster                                                      |
| chaos                   | 66.5 ms                                                | 48.1 ms: 1.38x faster                                                      |
| bench_mp_pool           | 40.8 ms                                                | 42.5 ms: 1.04x slower                                                      |
| bench_thread_pool       | 531 us                                                 | 447 us: 1.19x faster                                                       |
| coroutines              | 20.1 ms                                                | 18.6 ms: 1.08x faster                                                      |
| coverage                | 40.8 ms                                                | 57.4 ms: 1.41x slower                                                      |
| crypto_pyaes            | 77.9 ms                                                | 52.1 ms: 1.50x faster                                                      |
| deepcopy                | 278 us                                                 | 220 us: 1.27x faster                                                       |
| deepcopy_reduce         | 2.36 us                                                | 1.92 us: 1.23x faster                                                      |
| deepcopy_memo           | 34.4 us                                                | 26.1 us: 1.32x faster                                                      |
| deltablue               | 5.37 ms                                                | 2.59 ms: 2.07x faster                                                      |
| django_template         | 27.2 ms                                                | 21.1 ms: 1.29x faster                                                      |
| docutils                | 1.76 sec                                               | 1.45 sec: 1.22x faster                                                     |
| dulwich_log             | 36.4 ms                                                | 28.5 ms: 1.28x faster                                                      |
| fannkuch                | 318 ms                                                 | 255 ms: 1.24x faster                                                       |
| float                   | 72.1 ms                                                | 52.4 ms: 1.37x faster                                                      |
| generators              | 32.5 ms                                                | 34.4 ms: 1.06x slower                                                      |
| genshi_text             | 18.2 ms                                                | 14.8 ms: 1.23x faster                                                      |
| genshi_xml              | 37.7 ms                                                | 28.9 ms: 1.30x faster                                                      |
| go                      | 165 ms                                                 | 109 ms: 1.51x faster                                                       |
| hexiom                  | 6.31 ms                                                | 4.71 ms: 1.34x faster                                                      |
| html5lib                | 44.0 ms                                                | 34.9 ms: 1.26x faster                                                      |
| json                    | 3.13 ms                                                | 2.84 ms: 1.10x faster                                                      |
| json_dumps              | 8.34 ms                                                | 6.15 ms: 1.36x faster                                                      |
| json_loads              | 17.0 us                                                | 16.3 us: 1.05x faster                                                      |
| logging_format          | 4.95 us                                                | 3.87 us: 1.28x faster                                                      |
| logging_silent          | 119 ns                                                 | 66.0 ns: 1.81x faster                                                      |
| logging_simple          | 4.61 us                                                | 3.60 us: 1.28x faster                                                      |
| mako                    | 10.6 ms                                                | 7.29 ms: 1.45x faster                                                      |
| mdp                     | 1.66 sec                                               | 1.52 sec: 1.09x faster                                                     |
| meteor_contest          | 77.7 ms                                                | 73.0 ms: 1.07x faster                                                      |
| mypy                    | 521 ms                                                 | 414 ms: 1.26x faster                                                       |
| nbody                   | 94.6 ms                                                | 64.4 ms: 1.47x faster                                                      |
| nqueens                 | 68.6 ms                                                | 59.7 ms: 1.15x faster                                                      |
| pathlib                 | 22.2 ms                                                | 20.8 ms: 1.07x faster                                                      |
| pickle                  | 7.50 us                                                | 7.55 us: 1.01x slower                                                      |
| pickle_list             | 2.83 us                                                | 2.84 us: 1.01x slower                                                      |
| pickle_pure_python      | 284 us                                                 | 194 us: 1.46x faster                                                       |
| pidigits                | 284 ms                                                 | 283 ms: 1.00x faster                                                       |
| pprint_safe_repr        | 608 ms                                                 | 462 ms: 1.32x faster                                                       |
| pprint_pformat          | 1.24 sec                                               | 941 ms: 1.32x faster                                                       |
| pycparser               | 915 ms                                                 | 680 ms: 1.35x faster                                                       |
| pyflate                 | 454 ms                                                 | 322 ms: 1.41x faster                                                       |
| python_startup          | 9.59 ms                                                | 9.40 ms: 1.02x faster                                                      |
| python_startup_no_site  | 7.00 ms                                                | 7.38 ms: 1.05x slower                                                      |
| raytrace                | 329 ms                                                 | 210 ms: 1.57x faster                                                       |
| regex_compile           | 96.2 ms                                                | 73.6 ms: 1.31x faster                                                      |
| regex_dna               | 164 ms                                                 | 150 ms: 1.10x faster                                                       |
| regex_effbot            | 2.45 ms                                                | 2.61 ms: 1.06x slower                                                      |
| regex_v8                | 17.7 ms                                                | 16.1 ms: 1.10x faster                                                      |
| richards                | 51.4 ms                                                | 30.7 ms: 1.68x faster                                                      |
| scimark_fft             | 231 ms                                                 | 193 ms: 1.20x faster                                                       |
| scimark_lu              | 110 ms                                                 | 71.5 ms: 1.53x faster                                                      |
| scimark_monte_carlo     | 72.3 ms                                                | 45.7 ms: 1.58x faster                                                      |
| scimark_sor             | 126 ms                                                 | 85.2 ms: 1.48x faster                                                      |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.83 ms: 1.23x faster                                                      |
| spectral_norm           | 95.8 ms                                                | 72.8 ms: 1.32x faster                                                      |
| sqlglot_parse           | 1.33 ms                                                | 1.01 ms: 1.31x faster                                                      |
| sqlglot_transpile       | 1.54 ms                                                | 1.18 ms: 1.31x faster                                                      |
| sqlglot_optimize        | 38.1 ms                                                | 31.7 ms: 1.20x faster                                                      |
| sqlglot_normalize       | 198 ms                                                 | 174 ms: 1.14x faster                                                       |
| sqlite_synth            | 1.50 us                                                | 1.36 us: 1.10x faster                                                      |
| sympy_expand            | 275 ms                                                 | 241 ms: 1.14x faster                                                       |
| sympy_integrate         | 13.3 ms                                                | 11.2 ms: 1.19x faster                                                      |
| sympy_sum               | 93.5 ms                                                | 82.0 ms: 1.14x faster                                                      |
| sympy_str               | 169 ms                                                 | 145 ms: 1.17x faster                                                       |
| telco                   | 3.63 ms                                                | 3.39 ms: 1.07x faster                                                      |
| thrift                  | 577 us                                                 | 444 us: 1.30x faster                                                       |
| tornado_http            | 90.1 ms                                                | 70.2 ms: 1.28x faster                                                      |
| unpack_sequence         | 38.2 ns                                                | 33.6 ns: 1.14x faster                                                      |
| unpickle                | 10.0 us                                                | 9.87 us: 1.02x faster                                                      |
| unpickle_list           | 2.66 us                                                | 2.71 us: 1.02x slower                                                      |
| unpickle_pure_python    | 204 us                                                 | 145 us: 1.40x faster                                                       |
| xml_etree_parse         | 100 ms                                                 | 94.8 ms: 1.05x faster                                                      |
| xml_etree_iterparse     | 69.0 ms                                                | 68.3 ms: 1.01x faster                                                      |
| xml_etree_generate      | 54.5 ms                                                | 49.3 ms: 1.11x faster                                                      |
| xml_etree_process       | 45.1 ms                                                | 35.4 ms: 1.27x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.23x faster                                                               |

Benchmark hidden because not significant (1): pickle_dict
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20230126-3.12.0a4+-e69c1f3/bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3.json: asyncio_tcp, create_gc_cycles, dask, gc_traversal
