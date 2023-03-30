
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0b2
- machine: darwin-arm64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 162 ms: 1.24x faster                                       |
| chameleon      | 5.79 ms                                                | 4.60 ms: 1.26x faster                                      |
| docutils       | 1.78 sec                                               | 1.46 sec: 1.22x faster                                     |
| html5lib       | 44.2 ms                                                | 36.0 ms: 1.23x faster                                      |
| tornado_http   | 91.5 ms                                                | 70.8 ms: 1.29x faster                                      |
| Geometric mean | (ref)                                                  | 1.25x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 63.7 ms: 1.47x faster                                      |
| float          | 72.4 ms                                                | 55.2 ms: 1.31x faster                                      |
| pidigits       | 282 ms                                                 | 281 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.25x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 77.9 ms: 1.24x faster                                      |
| regex_v8       | 17.6 ms                                                | 16.1 ms: 1.09x faster                                      |
| regex_dna      | 162 ms                                                 | 150 ms: 1.08x faster                                       |
| regex_effbot   | 2.46 ms                                                | 2.40 ms: 1.02x faster                                      |
| Geometric mean | (ref)                                                  | 1.11x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 217 us: 1.31x faster                                       |
| xml_etree_process    | 44.8 ms                                                | 34.9 ms: 1.28x faster                                      |
| unpickle_pure_python | 203 us                                                 | 176 us: 1.15x faster                                       |
| xml_etree_generate   | 54.2 ms                                                | 48.2 ms: 1.12x faster                                      |
| json_dumps           | 8.40 ms                                                | 7.63 ms: 1.10x faster                                      |
| xml_etree_iterparse  | 72.3 ms                                                | 68.8 ms: 1.05x faster                                      |
| json_loads           | 16.9 us                                                | 16.1 us: 1.05x faster                                      |
| pickle_dict          | 17.9 us                                                | 17.2 us: 1.04x faster                                      |
| pickle               | 7.35 us                                                | 7.06 us: 1.04x faster                                      |
| pickle_list          | 2.80 us                                                | 2.76 us: 1.01x faster                                      |
| xml_etree_parse      | 106 ms                                                 | 105 ms: 1.01x faster                                       |
| Geometric mean       | (ref)                                                  | 1.09x faster                                               |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.5 ms: 1.05x slower                                      |
| python_startup_no_site | 8.88 ms                                                | 10.1 ms: 1.13x slower                                      |
| Geometric mean         | (ref)                                                  | 1.09x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 27.3 ms                                                | 20.9 ms: 1.30x faster                                      |
| mako            | 10.5 ms                                                | 8.36 ms: 1.25x faster                                      |
| genshi_xml      | 37.2 ms                                                | 30.3 ms: 1.22x faster                                      |
| genshi_text     | 18.4 ms                                                | 15.2 ms: 1.21x faster                                      |
| Geometric mean  | (ref)                                                  | 1.25x faster                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.79 ms: 1.84x faster                                      |
| logging_silent          | 119 ns                                                 | 65.3 ns: 1.83x faster                                      |
| scimark_sor             | 126 ms                                                 | 78.7 ms: 1.60x faster                                      |
| raytrace                | 325 ms                                                 | 205 ms: 1.59x faster                                       |
| go                      | 165 ms                                                 | 106 ms: 1.56x faster                                       |
| richards                | 51.4 ms                                                | 33.5 ms: 1.53x faster                                      |
| scimark_lu              | 109 ms                                                 | 71.3 ms: 1.53x faster                                      |
| crypto_pyaes            | 78.1 ms                                                | 51.5 ms: 1.52x faster                                      |
| scimark_monte_carlo     | 72.5 ms                                                | 48.7 ms: 1.49x faster                                      |
| nbody                   | 93.3 ms                                                | 63.7 ms: 1.47x faster                                      |
| pyflate                 | 453 ms                                                 | 315 ms: 1.44x faster                                       |
| async_tree_io           | 1.02 sec                                               | 711 ms: 1.43x faster                                       |
| async_tree_memoization  | 490 ms                                                 | 352 ms: 1.39x faster                                       |
| async_tree_none         | 400 ms                                                 | 291 ms: 1.38x faster                                       |
| chaos                   | 66.7 ms                                                | 49.5 ms: 1.35x faster                                      |
| hexiom                  | 6.32 ms                                                | 4.71 ms: 1.34x faster                                      |
| thrift                  | 580 us                                                 | 434 us: 1.34x faster                                       |
| logging_simple          | 4.63 us                                                | 3.48 us: 1.33x faster                                      |
| spectral_norm           | 95.8 ms                                                | 72.1 ms: 1.33x faster                                      |
| logging_format          | 4.97 us                                                | 3.76 us: 1.32x faster                                      |
| float                   | 72.4 ms                                                | 55.2 ms: 1.31x faster                                      |
| pickle_pure_python      | 283 us                                                 | 217 us: 1.31x faster                                       |
| pycparser               | 916 ms                                                 | 702 ms: 1.30x faster                                       |
| django_template         | 27.3 ms                                                | 20.9 ms: 1.30x faster                                      |
| tornado_http            | 91.5 ms                                                | 70.8 ms: 1.29x faster                                      |
| xml_etree_process       | 44.8 ms                                                | 34.9 ms: 1.28x faster                                      |
| chameleon               | 5.79 ms                                                | 4.60 ms: 1.26x faster                                      |
| mako                    | 10.5 ms                                                | 8.36 ms: 1.25x faster                                      |
| 2to3                    | 201 ms                                                 | 162 ms: 1.24x faster                                       |
| async_tree_cpu_io_mixed | 669 ms                                                 | 539 ms: 1.24x faster                                       |
| regex_compile           | 96.4 ms                                                | 77.9 ms: 1.24x faster                                      |
| pprint_safe_repr        | 606 ms                                                 | 490 ms: 1.24x faster                                       |
| mypy2                   | 307 ms                                                 | 249 ms: 1.23x faster                                       |
| html5lib                | 44.2 ms                                                | 36.0 ms: 1.23x faster                                      |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.25 ms: 1.23x faster                                      |
| pprint_pformat          | 1.23 sec                                               | 1.01 sec: 1.22x faster                                     |
| genshi_xml              | 37.2 ms                                                | 30.3 ms: 1.22x faster                                      |
| fannkuch                | 317 ms                                                 | 260 ms: 1.22x faster                                       |
| docutils                | 1.78 sec                                               | 1.46 sec: 1.22x faster                                     |
| dulwich_log             | 37.1 ms                                                | 30.4 ms: 1.22x faster                                      |
| sqlalchemy_declarative  | 74.9 ms                                                | 61.9 ms: 1.21x faster                                      |
| genshi_text             | 18.4 ms                                                | 15.2 ms: 1.21x faster                                      |
| create_gc_cycles        | 880 us                                                 | 730 us: 1.21x faster                                       |
| deepcopy_memo           | 34.4 us                                                | 28.8 us: 1.20x faster                                      |
| gunicorn                | 1.35 ms                                                | 1.14 ms: 1.19x faster                                      |
| aiohttp                 | 1.27 ms                                                | 1.07 ms: 1.19x faster                                      |
| sqlglot_optimize        | 38.0 ms                                                | 32.0 ms: 1.19x faster                                      |
| generators              | 32.7 ms                                                | 27.7 ms: 1.18x faster                                      |
| deepcopy                | 281 us                                                 | 238 us: 1.18x faster                                       |
| async_generators        | 234 ms                                                 | 199 ms: 1.18x faster                                       |
| coroutines              | 20.2 ms                                                | 17.3 ms: 1.17x faster                                      |
| dask                    | 265 ms                                                 | 227 ms: 1.17x faster                                       |
| bench_thread_pool       | 546 us                                                 | 468 us: 1.17x faster                                       |
| nqueens                 | 68.2 ms                                                | 58.5 ms: 1.17x faster                                      |
| unpack_sequence         | 37.4 ns                                                | 32.4 ns: 1.15x faster                                      |
| unpickle_pure_python    | 203 us                                                 | 176 us: 1.15x faster                                       |
| scimark_fft             | 230 ms                                                 | 200 ms: 1.15x faster                                       |
| deepcopy_reduce         | 2.37 us                                                | 2.06 us: 1.15x faster                                      |
| sqlglot_transpile       | 1.57 ms                                                | 1.37 ms: 1.15x faster                                      |
| sympy_integrate         | 13.3 ms                                                | 11.6 ms: 1.15x faster                                      |
| sqlglot_parse           | 1.37 ms                                                | 1.19 ms: 1.14x faster                                      |
| sqlglot_normalize       | 196 ms                                                 | 172 ms: 1.14x faster                                       |
| pylint                  | 307 ms                                                 | 270 ms: 1.14x faster                                       |
| sympy_sum               | 93.6 ms                                                | 82.7 ms: 1.13x faster                                      |
| sympy_expand            | 275 ms                                                 | 244 ms: 1.13x faster                                       |
| sympy_str               | 169 ms                                                 | 150 ms: 1.13x faster                                       |
| xml_etree_generate      | 54.2 ms                                                | 48.2 ms: 1.12x faster                                      |
| sqlite_synth            | 1.47 us                                                | 1.34 us: 1.10x faster                                      |
| json_dumps              | 8.40 ms                                                | 7.63 ms: 1.10x faster                                      |
| json                    | 3.08 ms                                                | 2.83 ms: 1.09x faster                                      |
| regex_v8                | 17.6 ms                                                | 16.1 ms: 1.09x faster                                      |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.19 ms: 1.08x faster                                      |
| mdp                     | 1.66 sec                                               | 1.54 sec: 1.08x faster                                     |
| regex_dna               | 162 ms                                                 | 150 ms: 1.08x faster                                       |
| telco                   | 3.63 ms                                                | 3.42 ms: 1.06x faster                                      |
| pathlib                 | 28.8 ms                                                | 27.4 ms: 1.05x faster                                      |
| xml_etree_iterparse     | 72.3 ms                                                | 68.8 ms: 1.05x faster                                      |
| json_loads              | 16.9 us                                                | 16.1 us: 1.05x faster                                      |
| pickle_dict             | 17.9 us                                                | 17.2 us: 1.04x faster                                      |
| pickle                  | 7.35 us                                                | 7.06 us: 1.04x faster                                      |
| asyncio_tcp             | 670 ms                                                 | 653 ms: 1.03x faster                                       |
| regex_effbot            | 2.46 ms                                                | 2.40 ms: 1.02x faster                                      |
| pickle_list             | 2.80 us                                                | 2.76 us: 1.01x faster                                      |
| xml_etree_parse         | 106 ms                                                 | 105 ms: 1.01x faster                                       |
| meteor_contest          | 78.1 ms                                                | 77.4 ms: 1.01x faster                                      |
| pidigits                | 282 ms                                                 | 281 ms: 1.01x faster                                       |
| gc_traversal            | 2.39 ms                                                | 2.41 ms: 1.01x slower                                      |
| comprehensions          | 17.6 us                                                | 18.3 us: 1.04x slower                                      |
| python_startup          | 11.9 ms                                                | 12.5 ms: 1.05x slower                                      |
| bench_mp_pool           | 39.7 ms                                                | 43.7 ms: 1.10x slower                                      |
| python_startup_no_site  | 8.88 ms                                                | 10.1 ms: 1.13x slower                                      |
| Geometric mean          | (ref)                                                  | 1.20x faster                                               |

Benchmark hidden because not significant (2): unpickle_list, unpickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: coverage, flaskblogging
