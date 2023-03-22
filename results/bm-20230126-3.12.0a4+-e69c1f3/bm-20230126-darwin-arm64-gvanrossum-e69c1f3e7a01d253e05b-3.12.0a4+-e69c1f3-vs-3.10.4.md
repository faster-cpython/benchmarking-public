
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
| 2to3           | 201 ms                                                 | 181 ms: 1.11x faster                                                       |
| chameleon      | 5.79 ms                                                | 4.58 ms: 1.27x faster                                                      |
| docutils       | 1.78 sec                                               | 1.45 sec: 1.23x faster                                                     |
| html5lib       | 44.2 ms                                                | 34.9 ms: 1.27x faster                                                      |
| tornado_http   | 91.5 ms                                                | 70.2 ms: 1.30x faster                                                      |
| Geometric mean | (ref)                                                  | 1.23x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 64.4 ms: 1.45x faster                                                      |
| float          | 72.4 ms                                                | 52.4 ms: 1.38x faster                                                      |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                  | 1.26x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 73.6 ms: 1.31x faster                                                      |
| regex_v8       | 17.6 ms                                                | 16.1 ms: 1.09x faster                                                      |
| regex_dna      | 162 ms                                                 | 150 ms: 1.08x faster                                                       |
| regex_effbot   | 2.46 ms                                                | 2.61 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 194 us: 1.46x faster                                                       |
| unpickle_pure_python | 203 us                                                 | 145 us: 1.40x faster                                                       |
| json_dumps           | 8.40 ms                                                | 6.15 ms: 1.37x faster                                                      |
| xml_etree_process    | 44.8 ms                                                | 35.4 ms: 1.27x faster                                                      |
| xml_etree_parse      | 106 ms                                                 | 94.8 ms: 1.12x faster                                                      |
| xml_etree_generate   | 54.2 ms                                                | 49.3 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 72.3 ms                                                | 68.3 ms: 1.06x faster                                                      |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                                      |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                                      |
| unpickle_list        | 2.69 us                                                | 2.71 us: 1.01x slower                                                      |
| pickle_list          | 2.80 us                                                | 2.84 us: 1.01x slower                                                      |
| pickle               | 7.35 us                                                | 7.55 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                               |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.40 ms: 1.27x faster                                                      |
| python_startup_no_site | 8.88 ms                                                | 7.38 ms: 1.20x faster                                                      |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.29 ms: 1.44x faster                                                      |
| django_template | 27.3 ms                                                | 21.1 ms: 1.29x faster                                                      |
| genshi_xml      | 37.2 ms                                                | 28.9 ms: 1.28x faster                                                      |
| genshi_text     | 18.4 ms                                                | 14.8 ms: 1.25x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.59 ms: 1.98x faster                                                      |
| logging_silent          | 119 ns                                                 | 66.0 ns: 1.81x faster                                                      |
| asyncio_tcp             | 670 ms                                                 | 395 ms: 1.70x faster                                                       |
| richards                | 51.4 ms                                                | 30.7 ms: 1.68x faster                                                      |
| scimark_monte_carlo     | 72.5 ms                                                | 45.7 ms: 1.59x faster                                                      |
| raytrace                | 325 ms                                                 | 210 ms: 1.55x faster                                                       |
| scimark_lu              | 109 ms                                                 | 71.5 ms: 1.53x faster                                                      |
| go                      | 165 ms                                                 | 109 ms: 1.52x faster                                                       |
| crypto_pyaes            | 78.1 ms                                                | 52.1 ms: 1.50x faster                                                      |
| scimark_sor             | 126 ms                                                 | 85.2 ms: 1.48x faster                                                      |
| async_tree_memoization  | 490 ms                                                 | 332 ms: 1.48x faster                                                       |
| pickle_pure_python      | 283 us                                                 | 194 us: 1.46x faster                                                       |
| nbody                   | 93.3 ms                                                | 64.4 ms: 1.45x faster                                                      |
| mako                    | 10.5 ms                                                | 7.29 ms: 1.44x faster                                                      |
| pyflate                 | 453 ms                                                 | 322 ms: 1.41x faster                                                       |
| unpickle_pure_python    | 203 us                                                 | 145 us: 1.40x faster                                                       |
| async_tree_none         | 400 ms                                                 | 288 ms: 1.39x faster                                                       |
| chaos                   | 66.7 ms                                                | 48.1 ms: 1.39x faster                                                      |
| pathlib                 | 28.8 ms                                                | 20.8 ms: 1.38x faster                                                      |
| float                   | 72.4 ms                                                | 52.4 ms: 1.38x faster                                                      |
| async_tree_io           | 1.02 sec                                               | 743 ms: 1.37x faster                                                       |
| json_dumps              | 8.40 ms                                                | 6.15 ms: 1.37x faster                                                      |
| sqlglot_parse           | 1.37 ms                                                | 1.01 ms: 1.35x faster                                                      |
| pycparser               | 916 ms                                                 | 680 ms: 1.35x faster                                                       |
| hexiom                  | 6.32 ms                                                | 4.71 ms: 1.34x faster                                                      |
| sqlglot_transpile       | 1.57 ms                                                | 1.18 ms: 1.34x faster                                                      |
| spectral_norm           | 95.8 ms                                                | 72.8 ms: 1.32x faster                                                      |
| deepcopy_memo           | 34.4 us                                                | 26.1 us: 1.32x faster                                                      |
| pprint_safe_repr        | 606 ms                                                 | 462 ms: 1.31x faster                                                       |
| regex_compile           | 96.4 ms                                                | 73.6 ms: 1.31x faster                                                      |
| pprint_pformat          | 1.23 sec                                               | 941 ms: 1.31x faster                                                       |
| thrift                  | 580 us                                                 | 444 us: 1.31x faster                                                       |
| tornado_http            | 91.5 ms                                                | 70.2 ms: 1.30x faster                                                      |
| dulwich_log             | 37.1 ms                                                | 28.5 ms: 1.30x faster                                                      |
| django_template         | 27.3 ms                                                | 21.1 ms: 1.29x faster                                                      |
| logging_simple          | 4.63 us                                                | 3.60 us: 1.29x faster                                                      |
| genshi_xml              | 37.2 ms                                                | 28.9 ms: 1.28x faster                                                      |
| logging_format          | 4.97 us                                                | 3.87 us: 1.28x faster                                                      |
| deepcopy                | 281 us                                                 | 220 us: 1.28x faster                                                       |
| html5lib                | 44.2 ms                                                | 34.9 ms: 1.27x faster                                                      |
| python_startup          | 11.9 ms                                                | 9.40 ms: 1.27x faster                                                      |
| xml_etree_process       | 44.8 ms                                                | 35.4 ms: 1.27x faster                                                      |
| chameleon               | 5.79 ms                                                | 4.58 ms: 1.27x faster                                                      |
| genshi_text             | 18.4 ms                                                | 14.8 ms: 1.25x faster                                                      |
| fannkuch                | 317 ms                                                 | 255 ms: 1.24x faster                                                       |
| create_gc_cycles        | 880 us                                                 | 711 us: 1.24x faster                                                       |
| deepcopy_reduce         | 2.37 us                                                | 1.92 us: 1.24x faster                                                      |
| async_tree_cpu_io_mixed | 669 ms                                                 | 544 ms: 1.23x faster                                                       |
| docutils                | 1.78 sec                                               | 1.45 sec: 1.23x faster                                                     |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.83 ms: 1.22x faster                                                      |
| bench_thread_pool       | 546 us                                                 | 447 us: 1.22x faster                                                       |
| python_startup_no_site  | 8.88 ms                                                | 7.38 ms: 1.20x faster                                                      |
| sqlglot_optimize        | 38.0 ms                                                | 31.7 ms: 1.20x faster                                                      |
| scimark_fft             | 230 ms                                                 | 193 ms: 1.20x faster                                                       |
| sympy_integrate         | 13.3 ms                                                | 11.2 ms: 1.19x faster                                                      |
| async_generators        | 234 ms                                                 | 200 ms: 1.17x faster                                                       |
| sympy_str               | 169 ms                                                 | 145 ms: 1.17x faster                                                       |
| sympy_expand            | 275 ms                                                 | 241 ms: 1.15x faster                                                       |
| nqueens                 | 68.2 ms                                                | 59.7 ms: 1.14x faster                                                      |
| sympy_sum               | 93.6 ms                                                | 82.0 ms: 1.14x faster                                                      |
| sqlglot_normalize       | 196 ms                                                 | 174 ms: 1.13x faster                                                       |
| xml_etree_parse         | 106 ms                                                 | 94.8 ms: 1.12x faster                                                      |
| unpack_sequence         | 37.4 ns                                                | 33.6 ns: 1.11x faster                                                      |
| 2to3                    | 201 ms                                                 | 181 ms: 1.11x faster                                                       |
| xml_etree_generate      | 54.2 ms                                                | 49.3 ms: 1.10x faster                                                      |
| mdp                     | 1.66 sec                                               | 1.52 sec: 1.09x faster                                                     |
| regex_v8                | 17.6 ms                                                | 16.1 ms: 1.09x faster                                                      |
| json                    | 3.08 ms                                                | 2.84 ms: 1.09x faster                                                      |
| sqlite_synth            | 1.47 us                                                | 1.36 us: 1.08x faster                                                      |
| coroutines              | 20.2 ms                                                | 18.6 ms: 1.08x faster                                                      |
| regex_dna               | 162 ms                                                 | 150 ms: 1.08x faster                                                       |
| telco                   | 3.63 ms                                                | 3.39 ms: 1.07x faster                                                      |
| meteor_contest          | 78.1 ms                                                | 73.0 ms: 1.07x faster                                                      |
| xml_etree_iterparse     | 72.3 ms                                                | 68.3 ms: 1.06x faster                                                      |
| json_loads              | 16.9 us                                                | 16.3 us: 1.04x faster                                                      |
| pidigits                | 282 ms                                                 | 283 ms: 1.00x slower                                                       |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                                      |
| unpickle_list           | 2.69 us                                                | 2.71 us: 1.01x slower                                                      |
| pickle_list             | 2.80 us                                                | 2.84 us: 1.01x slower                                                      |
| gc_traversal            | 2.39 ms                                                | 2.43 ms: 1.02x slower                                                      |
| pickle                  | 7.35 us                                                | 7.55 us: 1.03x slower                                                      |
| generators              | 32.7 ms                                                | 34.4 ms: 1.05x slower                                                      |
| regex_effbot            | 2.46 ms                                                | 2.61 ms: 1.06x slower                                                      |
| bench_mp_pool           | 39.7 ms                                                | 42.5 ms: 1.07x slower                                                      |
| dask                    | 265 ms                                                 | 317 ms: 1.20x slower                                                       |
| coverage                | 42.0 ms                                                | 57.4 ms: 1.37x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.23x faster                                                               |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, comprehensions, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230126-3.12.0a4+-e69c1f3/bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3.json: mypy
